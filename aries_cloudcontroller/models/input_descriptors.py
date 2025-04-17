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
from pydantic import BaseModel, Field, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.constraints import Constraints
from aries_cloudcontroller.models.schemas_input_descriptor_filter import (
    SchemasInputDescriptorFilter,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class InputDescriptors(BaseModel):
    """
    InputDescriptors
    """  # noqa: E501

    constraints: Optional[Constraints] = None
    group: Optional[List[StrictStr]] = None
    id: Optional[StrictStr] = Field(default=None, description="ID")
    metadata: Optional[Dict[str, Any]] = Field(
        default=None, description="Metadata dictionary"
    )
    name: Optional[StrictStr] = Field(default=None, description="Name")
    purpose: Optional[StrictStr] = Field(default=None, description="Purpose")
    var_schema: Optional[SchemasInputDescriptorFilter] = Field(
        default=None,
        description="Accepts a list of schema or a dict containing filters like oneof_filter.",
        alias="schema",
    )
    __properties: ClassVar[List[str]] = [
        "constraints",
        "group",
        "id",
        "metadata",
        "name",
        "purpose",
        "schema",
    ]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of InputDescriptors from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of constraints
        if self.constraints:
            _dict["constraints"] = self.constraints.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict["schema"] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InputDescriptors from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "constraints": (
                    Constraints.from_dict(obj["constraints"])
                    if obj.get("constraints") is not None
                    else None
                ),
                "group": obj.get("group"),
                "id": obj.get("id"),
                "metadata": obj.get("metadata"),
                "name": obj.get("name"),
                "purpose": obj.get("purpose"),
                "schema": (
                    SchemasInputDescriptorFilter.from_dict(obj["schema"])
                    if obj.get("schema") is not None
                    else None
                ),
            }
        )
        return _obj
