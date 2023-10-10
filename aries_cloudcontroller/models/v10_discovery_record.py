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


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from aries_cloudcontroller.models.disclose import Disclose
from aries_cloudcontroller.models.query import Query
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V10DiscoveryRecord(BaseModel):
    """
    V10DiscoveryRecord
    """
    connection_id: Optional[StrictStr] = Field(default=None, description="Connection identifier")
    created_at: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Time of record creation")
    disclose: Optional[Disclose] = None
    discovery_exchange_id: Optional[StrictStr] = Field(default=None, description="Credential exchange identifier")
    query_msg: Optional[Query] = None
    state: Optional[StrictStr] = Field(default=None, description="Current record state")
    thread_id: Optional[StrictStr] = Field(default=None, description="Thread identifier")
    trace: Optional[StrictBool] = Field(default=None, description="Record trace information, based on agent configuration")
    updated_at: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Time of last record update")
    __properties: ClassVar[List[str]] = ["connection_id", "created_at", "disclose", "discovery_exchange_id", "query_msg", "state", "thread_id", "trace", "updated_at"]

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
        """Create an instance of V10DiscoveryRecord from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of disclose
        if self.disclose:
            _dict['disclose'] = self.disclose.to_dict()
        # override the default output from pydantic by calling `to_dict()` of query_msg
        if self.query_msg:
            _dict['query_msg'] = self.query_msg.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of V10DiscoveryRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connection_id": obj.get("connection_id"),
            "created_at": obj.get("created_at"),
            "disclose": Disclose.from_dict(obj.get("disclose")) if obj.get("disclose") is not None else None,
            "discovery_exchange_id": obj.get("discovery_exchange_id"),
            "query_msg": Query.from_dict(obj.get("query_msg")) if obj.get("query_msg") is not None else None,
            "state": obj.get("state"),
            "thread_id": obj.get("thread_id"),
            "trace": obj.get("trace"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


