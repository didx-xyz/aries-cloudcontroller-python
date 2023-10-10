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

from pydantic import BaseModel, Field, StrictBool, StrictStr

from aries_cloudcontroller.models.v20_cred_filter import V20CredFilter
from aries_cloudcontroller.models.v20_cred_preview import V20CredPreview

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V20CredOfferRequest(BaseModel):
    """
    V20CredOfferRequest
    """
    auto_issue: Optional[StrictBool] = Field(default=None, description="Whether to respond automatically to credential requests, creating and issuing requested credentials")
    auto_remove: Optional[StrictBool] = Field(default=None, description="Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting)")
    comment: Optional[StrictStr] = Field(default=None, description="Human-readable comment")
    connection_id: StrictStr = Field(description="Connection identifier")
    credential_preview: Optional[V20CredPreview] = None
    filter: V20CredFilter
    replacement_id: Optional[StrictStr] = Field(default=None, description="Optional identifier used to manage credential replacement")
    trace: Optional[StrictBool] = Field(default=None, description="Record trace information, based on agent configuration")
    __properties: ClassVar[List[str]] = ["auto_issue", "auto_remove", "comment", "connection_id", "credential_preview", "filter", "replacement_id", "trace"]

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
        """Create an instance of V20CredOfferRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of credential_preview
        if self.credential_preview:
            _dict['credential_preview'] = self.credential_preview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if replacement_id (nullable) is None
        # and model_fields_set contains the field
        if self.replacement_id is None and "replacement_id" in self.model_fields_set:
            _dict['replacement_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of V20CredOfferRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auto_issue": obj.get("auto_issue"),
            "auto_remove": obj.get("auto_remove"),
            "comment": obj.get("comment"),
            "connection_id": obj.get("connection_id"),
            "credential_preview": V20CredPreview.from_dict(obj.get("credential_preview")) if obj.get("credential_preview") is not None else None,
            "filter": V20CredFilter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "replacement_id": obj.get("replacement_id"),
            "trace": obj.get("trace")
        })
        return _obj


