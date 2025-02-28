# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.2.1.post20250228
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.invitation_message import InvitationMessage
from aries_cloudcontroller.models.service_decorator import ServiceDecorator
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class OobRecord(BaseModel):
    """
    OobRecord
    """  # noqa: E501

    attach_thread_id: Optional[StrictStr] = Field(
        default=None, description="Connection record identifier"
    )
    connection_id: Optional[StrictStr] = Field(
        default=None, description="Connection record identifier"
    )
    created_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of record creation"
    )
    invi_msg_id: StrictStr = Field(description="Invitation message identifier")
    invitation: InvitationMessage = Field(description="Out of band invitation message")
    multi_use: Optional[StrictBool] = Field(
        default=None, description="Allow for multiple uses of the oob invitation"
    )
    oob_id: StrictStr = Field(description="Oob record identifier")
    our_recipient_key: Optional[StrictStr] = Field(
        default=None, description="Recipient key used for oob invitation"
    )
    role: Optional[StrictStr] = Field(default=None, description="OOB Role")
    state: StrictStr = Field(description="Out of band message exchange state")
    their_service: Optional[ServiceDecorator] = None
    trace: Optional[StrictBool] = Field(
        default=None,
        description="Record trace information, based on agent configuration",
    )
    updated_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of last record update"
    )
    __properties: ClassVar[List[str]] = [
        "attach_thread_id",
        "connection_id",
        "created_at",
        "invi_msg_id",
        "invitation",
        "multi_use",
        "oob_id",
        "our_recipient_key",
        "role",
        "state",
        "their_service",
        "trace",
        "updated_at",
    ]

    @field_validator("created_at")
    def created_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$/"
            )
        return value

    @field_validator("role")
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["sender", "receiver"]):
            raise ValueError("must be one of enum values ('sender', 'receiver')")
        return value

    @field_validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(
            [
                "initial",
                "prepare-response",
                "await-response",
                "reuse-not-accepted",
                "reuse-accepted",
                "done",
                "deleted",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('initial', 'prepare-response', 'await-response', 'reuse-not-accepted', 'reuse-accepted', 'done', 'deleted')"
            )
        return value

    @field_validator("updated_at")
    def updated_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$/"
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
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OobRecord from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of invitation
        if self.invitation:
            _dict["invitation"] = self.invitation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of their_service
        if self.their_service:
            _dict["their_service"] = self.their_service.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OobRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "attach_thread_id": obj.get("attach_thread_id"),
                "connection_id": obj.get("connection_id"),
                "created_at": obj.get("created_at"),
                "invi_msg_id": obj.get("invi_msg_id"),
                "invitation": (
                    InvitationMessage.from_dict(obj["invitation"])
                    if obj.get("invitation") is not None
                    else None
                ),
                "multi_use": obj.get("multi_use"),
                "oob_id": obj.get("oob_id"),
                "our_recipient_key": obj.get("our_recipient_key"),
                "role": obj.get("role"),
                "state": obj.get("state"),
                "their_service": (
                    ServiceDecorator.from_dict(obj["their_service"])
                    if obj.get("their_service") is not None
                    else None
                ),
                "trace": obj.get("trace"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
