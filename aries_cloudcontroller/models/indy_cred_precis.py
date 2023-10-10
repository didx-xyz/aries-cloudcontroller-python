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

from pydantic import BaseModel, StrictStr

from aries_cloudcontroller.models.indy_cred_info import IndyCredInfo
from aries_cloudcontroller.models.indy_non_revocation_interval import (
    IndyNonRevocationInterval,
)

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IndyCredPrecis(BaseModel):
    """
    IndyCredPrecis
    """
    cred_info: Optional[IndyCredInfo] = None
    interval: Optional[IndyNonRevocationInterval] = None
    presentation_referents: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["cred_info", "interval", "presentation_referents"]

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
        """Create an instance of IndyCredPrecis from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cred_info
        if self.cred_info:
            _dict['cred_info'] = self.cred_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interval
        if self.interval:
            _dict['interval'] = self.interval.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of IndyCredPrecis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cred_info": IndyCredInfo.from_dict(obj.get("cred_info")) if obj.get("cred_info") is not None else None,
            "interval": IndyNonRevocationInterval.from_dict(obj.get("interval")) if obj.get("interval") is not None else None,
            "presentation_referents": obj.get("presentation_referents")
        })
        return _obj


