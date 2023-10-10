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

from pydantic import BaseModel, StrictStr

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CredDefValueRevocation(BaseModel):
    """
    CredDefValueRevocation
    """

    g: Optional[StrictStr] = None
    g_dash: Optional[StrictStr] = None
    h: Optional[StrictStr] = None
    h0: Optional[StrictStr] = None
    h1: Optional[StrictStr] = None
    h2: Optional[StrictStr] = None
    h_cap: Optional[StrictStr] = None
    htilde: Optional[StrictStr] = None
    pk: Optional[StrictStr] = None
    u: Optional[StrictStr] = None
    y: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "g",
        "g_dash",
        "h",
        "h0",
        "h1",
        "h2",
        "h_cap",
        "htilde",
        "pk",
        "u",
        "y",
    ]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CredDefValueRevocation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of CredDefValueRevocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "g": obj.get("g"),
                "g_dash": obj.get("g_dash"),
                "h": obj.get("h"),
                "h0": obj.get("h0"),
                "h1": obj.get("h1"),
                "h2": obj.get("h2"),
                "h_cap": obj.get("h_cap"),
                "htilde": obj.get("htilde"),
                "pk": obj.get("pk"),
                "u": obj.get("u"),
                "y": obj.get("y"),
            }
        )
        return _obj
