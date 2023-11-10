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
import re
from typing import Any, ClassVar, Dict, List, Optional, Union

from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing_extensions import Annotated

from aries_cloudcontroller.models.attachment_def import AttachmentDef
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class InvitationCreateRequest(BaseModel):
    """
    InvitationCreateRequest
    """

    accept: Optional[List[StrictStr]] = Field(
        default=None,
        description="List of mime type in order of preference that should be use in responding to the message",
    )
    alias: Optional[StrictStr] = Field(default=None, description="Alias for connection")
    attachments: Optional[List[AttachmentDef]] = Field(
        default=None, description="Optional invitation attachments"
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
    mediation_id: Optional[StrictStr] = Field(
        default=None, description="Identifier for active mediation record to be used"
    )
    metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional metadata to attach to the connection created with the invitation",
    )
    my_label: Optional[StrictStr] = Field(
        default=None, description="Label for connection invitation"
    )
    protocol_version: Optional[StrictStr] = Field(
        default=None, description="OOB protocol version"
    )
    use_public_did: Optional[StrictBool] = Field(
        default=None, description="Whether to use public DID in invitation"
    )
    __properties: ClassVar[List[str]] = [
        "accept",
        "alias",
        "attachments",
        "goal",
        "goal_code",
        "handshake_protocols",
        "mediation_id",
        "metadata",
        "my_label",
        "protocol_version",
        "use_public_did",
    ]

    @field_validator("mediation_id")
    def mediation_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}/"
            )
        return value

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of InvitationCreateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item in self.attachments:
                if _item:
                    _items.append(_item.to_dict())
            _dict["attachments"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of InvitationCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "accept": obj.get("accept"),
                "alias": obj.get("alias"),
                "attachments": [
                    AttachmentDef.from_dict(_item) for _item in obj.get("attachments")
                ]
                if obj.get("attachments") is not None
                else None,
                "goal": obj.get("goal"),
                "goal_code": obj.get("goal_code"),
                "handshake_protocols": obj.get("handshake_protocols"),
                "mediation_id": obj.get("mediation_id"),
                "metadata": obj.get("metadata"),
                "my_label": obj.get("my_label"),
                "protocol_version": obj.get("protocol_version"),
                "use_public_did": obj.get("use_public_did"),
            }
        )
        return _obj
