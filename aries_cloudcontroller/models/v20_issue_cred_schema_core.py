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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from aries_cloudcontroller.models.v20_cred_filter import V20CredFilter
from aries_cloudcontroller.models.v20_cred_preview import V20CredPreview
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V20IssueCredSchemaCore(BaseModel):
    """
    V20IssueCredSchemaCore
    """
    auto_remove: Optional[StrictBool] = Field(default=None, description="Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting)")
    comment: Optional[StrictStr] = Field(default=None, description="Human-readable comment")
    credential_preview: Optional[V20CredPreview] = None
    filter: V20CredFilter
    replacement_id: Optional[StrictStr] = Field(default=None, description="Optional identifier used to manage credential replacement")
    trace: Optional[StrictBool] = Field(default=None, description="Record trace information, based on agent configuration")
    __properties: ClassVar[List[str]] = ["auto_remove", "comment", "credential_preview", "filter", "replacement_id", "trace"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V20IssueCredSchemaCore from a JSON string"""
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
        """Create an instance of V20IssueCredSchemaCore from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auto_remove": obj.get("auto_remove"),
            "comment": obj.get("comment"),
            "credential_preview": V20CredPreview.from_dict(obj.get("credential_preview")) if obj.get("credential_preview") is not None else None,
            "filter": V20CredFilter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "replacement_id": obj.get("replacement_id"),
            "trace": obj.get("trace")
        })
        return _obj

