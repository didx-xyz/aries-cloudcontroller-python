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

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RouteRecord(BaseModel):
    """
    RouteRecord
    """
    connection_id: Optional[StrictStr] = None
    created_at: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Time of record creation")
    recipient_key: StrictStr
    record_id: Optional[StrictStr] = None
    role: Optional[StrictStr] = None
    state: Optional[StrictStr] = Field(default=None, description="Current record state")
    updated_at: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Time of last record update")
    wallet_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["connection_id", "created_at", "recipient_key", "record_id", "role", "state", "updated_at", "wallet_id"]

    @field_validator('created_at')
    def created_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$/")
        return value

    @field_validator('updated_at')
    def updated_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$/")
        return value

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
        """Create an instance of RouteRecord from a JSON string"""
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
        """Create an instance of RouteRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connection_id": obj.get("connection_id"),
            "created_at": obj.get("created_at"),
            "recipient_key": obj.get("recipient_key"),
            "record_id": obj.get("record_id"),
            "role": obj.get("role"),
            "state": obj.get("state"),
            "updated_at": obj.get("updated_at"),
            "wallet_id": obj.get("wallet_id")
        })
        return _obj


