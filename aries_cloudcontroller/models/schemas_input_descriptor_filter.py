# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.3.0rc1.post20250417
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictBool
from typing_extensions import Self

from aries_cloudcontroller.models.schema_input_descriptor import SchemaInputDescriptor
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class SchemasInputDescriptorFilter(BaseModel):
    """
    SchemasInputDescriptorFilter
    """  # noqa: E501

    oneof_filter: Optional[StrictBool] = Field(default=None, description="oneOf")
    uri_groups: Optional[List[List[SchemaInputDescriptor]]] = None
    __properties: ClassVar[List[str]] = ["oneof_filter", "uri_groups"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SchemasInputDescriptorFilter from a JSON string"""
        return cls.from_dict(orjson.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in uri_groups (list of list)
        _items = []
        if self.uri_groups:
            for _item_uri_groups in self.uri_groups:
                if _item_uri_groups:
                    _items.append(
                        [
                            _inner_item.to_dict()
                            for _inner_item in _item_uri_groups
                            if _inner_item is not None
                        ]
                    )
            _dict["uri_groups"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SchemasInputDescriptorFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "oneof_filter": obj.get("oneof_filter"),
                "uri_groups": (
                    [
                        [
                            SchemaInputDescriptor.from_dict(_inner_item)
                            for _inner_item in _item
                        ]
                        for _item in obj["uri_groups"]
                    ]
                    if obj.get("uri_groups") is not None
                    else None
                ),
            }
        )
        return _obj
