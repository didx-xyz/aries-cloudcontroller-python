# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RevRegWalletUpdatedResult(BaseModel):
    """
    RevRegWalletUpdatedResult
    """
    accum_calculated: Optional[Union[str, Any]] = Field(default=None, description="Calculated accumulator for phantom revocations")
    accum_fixed: Optional[Union[str, Any]] = Field(default=None, description="Applied ledger transaction to fix revocations")
    rev_reg_delta: Optional[Union[str, Any]] = Field(default=None, description="Indy revocation registry delta")
    __properties: ClassVar[List[str]] = ["accum_calculated", "accum_fixed", "rev_reg_delta"]

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
        """Create an instance of RevRegWalletUpdatedResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of RevRegWalletUpdatedResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accum_calculated": obj.get("accum_calculated"),
            "accum_fixed": obj.get("accum_fixed"),
            "rev_reg_delta": obj.get("rev_reg_delta")
        })
        return _obj


