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

from pydantic import BaseModel, Field, StrictStr

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class V10CredentialIssueRequest(BaseModel):
    """
    V10CredentialIssueRequest
    """

    comment: Optional[StrictStr] = Field(
        default=None, description="Human-readable comment"
    )
    __properties: ClassVar[List[str]] = ["comment"]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.model_dump_json(self.to_dict(), by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V10CredentialIssueRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude={}, exclude_none=True)
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict["comment"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of V10CredentialIssueRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({"comment": obj.get("comment")})
        return _obj
