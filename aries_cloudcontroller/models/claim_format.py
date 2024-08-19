# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel
from typing_extensions import Self

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class ClaimFormat(BaseModel):
    """
    ClaimFormat
    """  # noqa: E501

    di_vc: Optional[Dict[str, Any]] = None
    jwt: Optional[Dict[str, Any]] = None
    jwt_vc: Optional[Dict[str, Any]] = None
    jwt_vp: Optional[Dict[str, Any]] = None
    ldp: Optional[Dict[str, Any]] = None
    ldp_vc: Optional[Dict[str, Any]] = None
    ldp_vp: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = [
        "di_vc",
        "jwt",
        "jwt_vc",
        "jwt_vp",
        "ldp",
        "ldp_vc",
        "ldp_vp",
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
        """Create an instance of ClaimFormat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClaimFormat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "di_vc": obj.get("di_vc"),
                "jwt": obj.get("jwt"),
                "jwt_vc": obj.get("jwt_vc"),
                "jwt_vp": obj.get("jwt_vp"),
                "ldp": obj.get("ldp"),
                "ldp_vc": obj.get("ldp_vc"),
                "ldp_vp": obj.get("ldp_vp"),
            }
        )
        return _obj
