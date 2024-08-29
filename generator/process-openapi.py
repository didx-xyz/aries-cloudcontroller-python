import re
from functools import singledispatchmethod

import deepmerge
import yaml


class OpenAPICleaner:
    FIX_REF_RE = re.compile(r"#/definitions")

    @singledispatchmethod
    def no_null_descriptions(self, value):
        return value

    @no_null_descriptions.register
    def _(self, value: dict):
        for child in value.values():
            self.no_null_descriptions(child)

        if "description" in value and value["description"] is None:
            value["description"] = ""

    @no_null_descriptions.register
    def _(self, value: list):
        for item in value:
            self.no_null_descriptions(item)

    @singledispatchmethod
    def no_missing_external_doc_urls(self, value):
        return value

    @no_missing_external_doc_urls.register
    def _(self, value: dict):
        for child in value.values():
            self.no_missing_external_doc_urls(child)

        if "externalDocs" in value and "url" not in value["externalDocs"]:
            value["externalDocs"]["url"] = "https://example.com/replace/me"

    @no_missing_external_doc_urls.register
    def _(self, value: list):
        for item in value:
            self.no_missing_external_doc_urls(item)

    @singledispatchmethod
    def fix_refs(self, value):
        return value

    @fix_refs.register
    def _(self, value: dict):
        for child in value.values():
            self.fix_refs(child)

        if "$ref" in value:
            value["$ref"] = self.FIX_REF_RE.sub("#/components/schemas", value["$ref"])

    @fix_refs.register
    def _(self, value: list):
        for item in value:
            self.fix_refs(item)

    @singledispatchmethod
    def fix_content_types(self, value):
        return value

    @fix_content_types.register
    def _(self, value: dict):
        for child in value.values():
            self.fix_content_types(child)

        if "*/*" in value:
            value["application/json"] = value["*/*"]
            del value["*/*"]

    @fix_content_types.register
    def _(self, value: list):
        for item in value:
            self.fix_content_types(item)

    @singledispatchmethod
    def fix_vc_api(self, value):
        return value

    @fix_vc_api.register
    def _(self, value: dict):
        for key, child in value.items():
            value[key] = self.fix_vc_api(child)
        return value

    @fix_vc_api.register
    def _(self, value: list):
        return [self.fix_vc_api(item) for item in value]

    @fix_vc_api.register
    def _(self, value: str):
        if "https" not in value:
            return value.replace("vc-api", "vc")
        else:
            return value

    def clean(self, value):
        self.no_null_descriptions(value)
        self.no_missing_external_doc_urls(value)
        self.fix_refs(value)
        self.fix_content_types(value)
        self.fix_vc_api(value)


def load_yaml_file(file_path):
    with open(file_path, "r") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def save_yaml_file(data, file_path):
    with open(file_path, "w") as file:
        yaml.dump(data, file, sort_keys=False)


def merge_operation_ids(openapi_path, ops_map_path):
    openapi = load_yaml_file(openapi_path)
    ops = load_yaml_file(ops_map_path)
    return deepmerge.always_merger.merge(openapi, ops)


def find_missing_operation_ids(openapi_path, ops_map_path):
    openapi = load_yaml_file(openapi_path)
    existing_ops = load_yaml_file(ops_map_path)

    missing_ops = {"paths": {}}

    for path, methods in openapi.get("paths", {}).items():
        if path not in existing_ops.get("paths", {}):
            missing_ops["paths"][path] = {}
            for method, details in methods.items():
                # Placeholder operationId can be a formatted string or a more sophisticated naming convention
                path_r = path.replace("/", "_").replace("-", "_")
                missing_ops["paths"][path][method] = {
                    "operationId": f"{method}_{path_r.strip('_')}"
                }
        else:
            for method in methods:
                if method not in existing_ops["paths"][path]:
                    if path not in missing_ops["paths"]:
                        missing_ops["paths"][path] = {}
                    # Adding default or placeholder operation ID for new methods in existing paths
                    missing_ops["paths"][path][method] = {
                        "operationId": f"{method}_{path.replace('/', '_').strip('_')}"
                    }
    if missing_ops["paths"]:
        return missing_ops
    else:
        return None


if __name__ == "__main__":
    openapi_path = "/app/openapi.yml"
    ops_map_path = "/app/operation-id-map.yml"
    new_ops_map_path = "/app/operation-id-map-new.yml"

    # Optionally merge and clean current specs
    result = merge_operation_ids(openapi_path, ops_map_path)
    cleaner = OpenAPICleaner()
    cleaner.clean(result)
    save_yaml_file(result, openapi_path)

    # Find and save new operation IDs
    new_ops = find_missing_operation_ids(openapi_path, ops_map_path)
    if new_ops:
        print("Missing operation ids detected")
        save_yaml_file(new_ops, new_ops_map_path)
