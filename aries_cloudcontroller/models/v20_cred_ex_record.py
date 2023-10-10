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

from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing_extensions import Annotated

from aries_cloudcontroller.models.v20_cred_ex_record_by_format import (
    V20CredExRecordByFormat,
)
from aries_cloudcontroller.models.v20_cred_issue import V20CredIssue
from aries_cloudcontroller.models.v20_cred_offer import V20CredOffer
from aries_cloudcontroller.models.v20_cred_preview import V20CredPreview
from aries_cloudcontroller.models.v20_cred_proposal import V20CredProposal
from aries_cloudcontroller.models.v20_cred_request import V20CredRequest

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class V20CredExRecord(BaseModel):
    """
    V20CredExRecord
    """

    auto_issue: Optional[StrictBool] = Field(
        default=None,
        description="Issuer choice to issue to request in this credential exchange",
    )
    auto_offer: Optional[StrictBool] = Field(
        default=None,
        description="Holder choice to accept offer in this credential exchange",
    )
    auto_remove: Optional[StrictBool] = Field(
        default=None,
        description="Issuer choice to remove this credential exchange record when complete",
    )
    by_format: Optional[V20CredExRecordByFormat] = None
    connection_id: Optional[StrictStr] = Field(
        default=None, description="Connection identifier"
    )
    created_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of record creation"
    )
    cred_ex_id: Optional[StrictStr] = Field(
        default=None, description="Credential exchange identifier"
    )
    cred_issue: Optional[V20CredIssue] = None
    cred_offer: Optional[V20CredOffer] = None
    cred_preview: Optional[V20CredPreview] = None
    cred_proposal: Optional[V20CredProposal] = None
    cred_request: Optional[V20CredRequest] = None
    error_msg: Optional[StrictStr] = Field(default=None, description="Error message")
    initiator: Optional[StrictStr] = Field(
        default=None,
        description="Issue-credential exchange initiator: self or external",
    )
    parent_thread_id: Optional[StrictStr] = Field(
        default=None, description="Parent thread identifier"
    )
    role: Optional[StrictStr] = Field(
        default=None, description="Issue-credential exchange role: holder or issuer"
    )
    state: Optional[StrictStr] = Field(
        default=None, description="Issue-credential exchange state"
    )
    thread_id: Optional[StrictStr] = Field(
        default=None, description="Thread identifier"
    )
    trace: Optional[StrictBool] = Field(
        default=None,
        description="Record trace information, based on agent configuration",
    )
    updated_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of last record update"
    )
    __properties: ClassVar[List[str]] = [
        "auto_issue",
        "auto_offer",
        "auto_remove",
        "by_format",
        "connection_id",
        "created_at",
        "cred_ex_id",
        "cred_issue",
        "cred_offer",
        "cred_preview",
        "cred_proposal",
        "cred_request",
        "error_msg",
        "initiator",
        "parent_thread_id",
        "role",
        "state",
        "thread_id",
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

    @field_validator("initiator")
    def initiator_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("self", "external"):
            raise ValueError("must be one of enum values ('self', 'external')")
        return value

    @field_validator("role")
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("issuer", "holder"):
            raise ValueError("must be one of enum values ('issuer', 'holder')")
        return value

    @field_validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (
            "proposal-sent",
            "proposal-received",
            "offer-sent",
            "offer-received",
            "request-sent",
            "request-received",
            "credential-issued",
            "credential-received",
            "done",
            "credential-revoked",
            "abandoned",
            "deleted",
        ):
            raise ValueError(
                "must be one of enum values ('proposal-sent', 'proposal-received', 'offer-sent', 'offer-received', 'request-sent', 'request-received', 'credential-issued', 'credential-received', 'done', 'credential-revoked', 'abandoned', 'deleted')"
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

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V20CredExRecord from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of by_format
        if self.by_format:
            _dict["by_format"] = self.by_format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cred_issue
        if self.cred_issue:
            _dict["cred_issue"] = self.cred_issue.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cred_offer
        if self.cred_offer:
            _dict["cred_offer"] = self.cred_offer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cred_preview
        if self.cred_preview:
            _dict["cred_preview"] = self.cred_preview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cred_proposal
        if self.cred_proposal:
            _dict["cred_proposal"] = self.cred_proposal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cred_request
        if self.cred_request:
            _dict["cred_request"] = self.cred_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of V20CredExRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "auto_issue": obj.get("auto_issue"),
                "auto_offer": obj.get("auto_offer"),
                "auto_remove": obj.get("auto_remove"),
                "by_format": V20CredExRecordByFormat.from_dict(obj.get("by_format"))
                if obj.get("by_format") is not None
                else None,
                "connection_id": obj.get("connection_id"),
                "created_at": obj.get("created_at"),
                "cred_ex_id": obj.get("cred_ex_id"),
                "cred_issue": V20CredIssue.from_dict(obj.get("cred_issue"))
                if obj.get("cred_issue") is not None
                else None,
                "cred_offer": V20CredOffer.from_dict(obj.get("cred_offer"))
                if obj.get("cred_offer") is not None
                else None,
                "cred_preview": V20CredPreview.from_dict(obj.get("cred_preview"))
                if obj.get("cred_preview") is not None
                else None,
                "cred_proposal": V20CredProposal.from_dict(obj.get("cred_proposal"))
                if obj.get("cred_proposal") is not None
                else None,
                "cred_request": V20CredRequest.from_dict(obj.get("cred_request"))
                if obj.get("cred_request") is not None
                else None,
                "error_msg": obj.get("error_msg"),
                "initiator": obj.get("initiator"),
                "parent_thread_id": obj.get("parent_thread_id"),
                "role": obj.get("role"),
                "state": obj.get("state"),
                "thread_id": obj.get("thread_id"),
                "trace": obj.get("trace"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
