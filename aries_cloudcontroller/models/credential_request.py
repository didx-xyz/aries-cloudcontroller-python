import json
import logging

logger = logging.getLogger("aries_controller.models.credential_request")


class CredentialRequest:
    def __init__(self, credential_request_json):
        try:
            self.json_data = json.loads(credential_request_json)
        except Exception:
            logger.error("Failed to load credentials request JSON")
            raise
        self.validate_credential_request_json(credential_request_json)

    def get_type(self):
        return self.json_data["@type"]

    def get_id(self):
        return self.json_data["@id"]

    def get_goal_code(self):
        return self.json_data["goal_code"]

    def get_comments(self):
        return self.json_data["comment"]

    def get_formats(self):
        return self.json_data["formats"]

    def get_attachments(self):
        return self.json_data["requests~attach"]

    def validate_credential_request_json(self, presentation_json):
        try:
            # Taken from sample response in swagger UI
            # TODO Determine whether this is the minimal set of keys
            presentation_keys = [
                "@type",
                "@id",
                "goal_code",
                "comment",
                "formats",
                "requests~attach",
            ]
            for key in presentation_keys:
                assert key in json.loads(
                    presentation_json
                ), f"Invalid proof request. Missing key {key}"
        except AssertionError:
            raise
