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
import re  # noqa: F401
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class PublishRevocations(BaseModel):
    """
    PublishRevocations
    """

    rrid2crid: Optional[Dict[str, List[Annotated[str, Field(strict=True)]]]] = Field(
        default=None, description="Credential revocation ids by revocation registry id"
    )
    __properties: ClassVar[List[str]] = ["rrid2crid"]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.model_dump_json(self.to_dict(), by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PublishRevocations from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in rrid2crid (dict of array)
        _field_dict_of_array = {}
        if self.rrid2crid:
            for _key in self.rrid2crid:
                if self.rrid2crid[_key]:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.rrid2crid[_key]
                    ]
            _dict["rrid2crid"] = _field_dict_of_array
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of PublishRevocations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({"rrid2crid": obj.get("rrid2crid")})
        return _obj
