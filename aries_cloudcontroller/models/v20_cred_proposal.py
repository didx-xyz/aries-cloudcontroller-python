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

from pydantic import BaseModel, Field, StrictStr

from aries_cloudcontroller.models.attach_decorator import AttachDecorator
from aries_cloudcontroller.models.v20_cred_format import V20CredFormat
from aries_cloudcontroller.models.v20_cred_preview import V20CredPreview

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class V20CredProposal(BaseModel):
    """
    V20CredProposal
    """

    id: Optional[StrictStr] = Field(
        default=None, description="Message identifier", alias="@id"
    )
    type: Optional[StrictStr] = Field(
        default=None, description="Message type", alias="@type"
    )
    comment: Optional[StrictStr] = Field(
        default=None, description="Human-readable comment"
    )
    credential_preview: Optional[V20CredPreview] = None
    filtersattach: List[AttachDecorator] = Field(
        description="Credential filter per acceptable format on corresponding identifier",
        alias="filters~attach",
    )
    formats: List[V20CredFormat] = Field(description="Attachment formats")
    __properties: ClassVar[List[str]] = [
        "@id",
        "@type",
        "comment",
        "credential_preview",
        "filters~attach",
        "formats",
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
        """Create an instance of V20CredProposal from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "type",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of credential_preview
        if self.credential_preview:
            _dict["credential_preview"] = self.credential_preview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in filtersattach (list)
        _items = []
        if self.filtersattach:
            for _item in self.filtersattach:
                if _item:
                    _items.append(_item.to_dict())
            _dict["filters~attach"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in formats (list)
        _items = []
        if self.formats:
            for _item in self.formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict["formats"] = _items
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict["comment"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of V20CredProposal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@id": obj.get("@id"),
                "@type": obj.get("@type"),
                "comment": obj.get("comment"),
                "credential_preview": V20CredPreview.from_dict(
                    obj.get("credential_preview")
                )
                if obj.get("credential_preview") is not None
                else None,
                "filters~attach": [
                    AttachDecorator.from_dict(_item)
                    for _item in obj.get("filters~attach")
                ]
                if obj.get("filters~attach") is not None
                else None,
                "formats": [
                    V20CredFormat.from_dict(_item) for _item in obj.get("formats")
                ]
                if obj.get("formats") is not None
                else None,
            }
        )
        return _obj
