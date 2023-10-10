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
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field

from aries_cloudcontroller.models.indy_rev_reg_def_value_public_keys_accum_key import (
    IndyRevRegDefValuePublicKeysAccumKey,
)

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IndyRevRegDefValuePublicKeys(BaseModel):
    """
    IndyRevRegDefValuePublicKeys
    """
    accum_key: Optional[IndyRevRegDefValuePublicKeysAccumKey] = Field(default=None, alias="accumKey")
    __properties: ClassVar[List[str]] = ["accumKey"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.model_dump_json(self.to_dict(), by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IndyRevRegDefValuePublicKeys from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of accum_key
        if self.accum_key:
            _dict['accumKey'] = self.accum_key.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of IndyRevRegDefValuePublicKeys from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accumKey": IndyRevRegDefValuePublicKeysAccumKey.from_dict(obj.get("accumKey")) if obj.get("accumKey") is not None else None
        })
        return _obj


