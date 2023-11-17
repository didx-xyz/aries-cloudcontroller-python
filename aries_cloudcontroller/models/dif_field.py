# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictStr, field_validator

from aries_cloudcontroller.models.filter import Filter
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class DIFField(BaseModel):
    """
    DIFField
    """  # noqa: E501

    filter: Optional[Filter] = None
    id: Optional[StrictStr] = Field(default=None, description="ID")
    path: Optional[List[StrictStr]] = None
    predicate: Optional[StrictStr] = Field(default=None, description="Preference")
    purpose: Optional[StrictStr] = Field(default=None, description="Purpose")
    __properties: ClassVar[List[str]] = ["filter", "id", "path", "predicate", "purpose"]

    @field_validator("predicate")
    def predicate_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("required", "preferred"):
            raise ValueError("must be one of enum values ('required', 'preferred')")
        return value

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DIFField from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict["filter"] = self.filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DIFField from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "filter": Filter.from_dict(obj.get("filter"))
                if obj.get("filter") is not None
                else None,
                "id": obj.get("id"),
                "path": obj.get("path"),
                "predicate": obj.get("predicate"),
                "purpose": obj.get("purpose"),
            }
        )
        return _obj
