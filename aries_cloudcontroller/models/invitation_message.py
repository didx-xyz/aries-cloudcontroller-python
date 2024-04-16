# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from pydantic import BaseModel, Field, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.attach_decorator import AttachDecorator
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class InvitationMessage(BaseModel):
    """
    InvitationMessage
    """  # noqa: E501

    id: Optional[StrictStr] = Field(
        default=None, description="Message identifier", alias="@id"
    )
    type: Optional[StrictStr] = Field(
        default=None, description="Message type", alias="@type"
    )
    accept: Optional[List[StrictStr]] = Field(
        default=None, description="List of mime type in order of preference"
    )
    goal: Optional[StrictStr] = Field(
        default=None,
        description="A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message",
    )
    goal_code: Optional[StrictStr] = Field(
        default=None,
        description="A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message",
    )
    handshake_protocols: Optional[List[StrictStr]] = None
    image_url: Optional[StrictStr] = Field(
        default=None,
        description="Optional image URL for out-of-band invitation",
        alias="imageUrl",
    )
    label: Optional[StrictStr] = Field(default=None, description="Optional label")
    requestsattach: Optional[List[AttachDecorator]] = Field(
        default=None, description="Optional request attachment", alias="requests~attach"
    )
    services: Optional[List[Union[str, Dict]]] = None
    __properties: ClassVar[List[str]] = [
        "@id",
        "@type",
        "accept",
        "goal",
        "goal_code",
        "handshake_protocols",
        "imageUrl",
        "label",
        "requests~attach",
        "services",
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
        """Create an instance of InvitationMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in requestsattach (list)
        _items = []
        if self.requestsattach:
            for _item in self.requestsattach:
                if _item:
                    _items.append(_item.to_dict())
            _dict["requests~attach"] = _items
        # set to None if image_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_url is None and "image_url" in self.model_fields_set:
            _dict["imageUrl"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvitationMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@id": obj.get("@id"),
                "@type": obj.get("@type"),
                "accept": obj.get("accept"),
                "goal": obj.get("goal"),
                "goal_code": obj.get("goal_code"),
                "handshake_protocols": obj.get("handshake_protocols"),
                "imageUrl": obj.get("imageUrl"),
                "label": obj.get("label"),
                "requests~attach": (
                    [
                        AttachDecorator.from_dict(_item)
                        for _item in obj["requests~attach"]
                    ]
                    if obj.get("requests~attach") is not None
                    else None
                ),
                "services": obj.get("services"),
            }
        )
        return _obj
