# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.3.0.post20250507
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.attach_decorator import AttachDecorator
from aries_cloudcontroller.models.credential_preview import CredentialPreview
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class CredentialOffer(BaseModel):
    """
    CredentialOffer
    """  # noqa: E501

    id: Optional[StrictStr] = Field(
        default=None, description="Message identifier", alias="@id"
    )
    type: Optional[StrictStr] = Field(
        default=None, description="Message type", alias="@type"
    )
    comment: Optional[StrictStr] = Field(
        default=None, description="Human-readable comment"
    )
    credential_preview: Optional[CredentialPreview] = None
    offersattach: List[AttachDecorator] = Field(alias="offers~attach")
    __properties: ClassVar[List[str]] = [
        "@id",
        "@type",
        "comment",
        "credential_preview",
        "offers~attach",
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
        """Create an instance of CredentialOffer from a JSON string"""
        return cls.from_dict(orjson.loads(json_str))

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
        # override the default output from pydantic by calling `to_dict()` of credential_preview
        if self.credential_preview:
            _dict["credential_preview"] = self.credential_preview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in offersattach (list)
        _items = []
        if self.offersattach:
            for _item_offersattach in self.offersattach:
                if _item_offersattach:
                    _items.append(_item_offersattach.to_dict())
            _dict["offers~attach"] = _items
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict["comment"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CredentialOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@id": obj.get("@id"),
                "@type": obj.get("@type"),
                "comment": obj.get("comment"),
                "credential_preview": (
                    CredentialPreview.from_dict(obj["credential_preview"])
                    if obj.get("credential_preview") is not None
                    else None
                ),
                "offers~attach": (
                    [AttachDecorator.from_dict(_item) for _item in obj["offers~attach"]]
                    if obj.get("offers~attach") is not None
                    else None
                ),
            }
        )
        return _obj
