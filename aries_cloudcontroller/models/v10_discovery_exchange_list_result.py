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

from pydantic import BaseModel

from aries_cloudcontroller.models.v10_discovery_record import V10DiscoveryRecord

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class V10DiscoveryExchangeListResult(BaseModel):
    """
    V10DiscoveryExchangeListResult
    """

    results: Optional[List[V10DiscoveryRecord]] = None
    __properties: ClassVar[List[str]] = ["results"]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.model_dump_json(self.to_dict(), by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V10DiscoveryExchangeListResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict["results"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of V10DiscoveryExchangeListResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "results": [
                    V10DiscoveryRecord.from_dict(_item) for _item in obj.get("results")
                ]
                if obj.get("results") is not None
                else None
            }
        )
        return _obj
