# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.1.1b0
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

from aries_cloudcontroller.models.indy_proof import IndyProof
from aries_cloudcontroller.models.indy_proof_request import IndyProofRequest
from aries_cloudcontroller.models.presentation_proposal import PresentationProposal
from aries_cloudcontroller.models.presentation_request import PresentationRequest
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class V10PresentationExchange(BaseModel):
    """
    V10PresentationExchange
    """  # noqa: E501

    auto_present: Optional[StrictBool] = Field(
        default=None,
        description="Prover choice to auto-present proof as verifier requests",
    )
    auto_remove: Optional[StrictBool] = Field(
        default=None,
        description="Verifier choice to remove this presentation exchange record when complete",
    )
    auto_verify: Optional[StrictBool] = Field(
        default=None, description="Verifier choice to auto-verify proof presentation"
    )
    connection_id: Optional[StrictStr] = Field(
        default=None, description="Connection identifier"
    )
    created_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of record creation"
    )
    error_msg: Optional[StrictStr] = Field(default=None, description="Error message")
    initiator: Optional[StrictStr] = Field(
        default=None, description="Present-proof exchange initiator: self or external"
    )
    presentation: Optional[IndyProof] = Field(
        default=None, description="(Indy) presentation (also known as proof)"
    )
    presentation_exchange_id: Optional[StrictStr] = Field(
        default=None, description="Presentation exchange identifier"
    )
    presentation_proposal_dict: Optional[PresentationProposal] = Field(
        default=None, description="Presentation proposal message"
    )
    presentation_request: Optional[IndyProofRequest] = Field(
        default=None,
        description="(Indy) presentation request (also known as proof request)",
    )
    presentation_request_dict: Optional[PresentationRequest] = Field(
        default=None, description="Presentation request message"
    )
    role: Optional[StrictStr] = Field(
        default=None, description="Present-proof exchange role: prover or verifier"
    )
    state: Optional[StrictStr] = Field(
        default=None, description="Present-proof exchange state"
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
    verified: Optional[StrictStr] = Field(
        default=None, description="Whether presentation is verified: true or false"
    )
    verified_msgs: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = [
        "auto_present",
        "auto_remove",
        "auto_verify",
        "connection_id",
        "created_at",
        "error_msg",
        "initiator",
        "presentation",
        "presentation_exchange_id",
        "presentation_proposal_dict",
        "presentation_request",
        "presentation_request_dict",
        "role",
        "state",
        "thread_id",
        "trace",
        "updated_at",
        "verified",
        "verified_msgs",
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

        if value not in set(["self", "external"]):
            raise ValueError("must be one of enum values ('self', 'external')")
        return value

    @field_validator("role")
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["prover", "verifier"]):
            raise ValueError("must be one of enum values ('prover', 'verifier')")
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

    @field_validator("verified")
    def verified_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["true", "false"]):
            raise ValueError("must be one of enum values ('true', 'false')")
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
        """Create an instance of V10PresentationExchange from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of presentation
        if self.presentation:
            _dict["presentation"] = self.presentation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of presentation_proposal_dict
        if self.presentation_proposal_dict:
            _dict["presentation_proposal_dict"] = (
                self.presentation_proposal_dict.to_dict()
            )
        # override the default output from pydantic by calling `to_dict()` of presentation_request
        if self.presentation_request:
            _dict["presentation_request"] = self.presentation_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of presentation_request_dict
        if self.presentation_request_dict:
            _dict["presentation_request_dict"] = (
                self.presentation_request_dict.to_dict()
            )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V10PresentationExchange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "auto_present": obj.get("auto_present"),
                "auto_remove": obj.get("auto_remove"),
                "auto_verify": obj.get("auto_verify"),
                "connection_id": obj.get("connection_id"),
                "created_at": obj.get("created_at"),
                "error_msg": obj.get("error_msg"),
                "initiator": obj.get("initiator"),
                "presentation": (
                    IndyProof.from_dict(obj["presentation"])
                    if obj.get("presentation") is not None
                    else None
                ),
                "presentation_exchange_id": obj.get("presentation_exchange_id"),
                "presentation_proposal_dict": (
                    PresentationProposal.from_dict(obj["presentation_proposal_dict"])
                    if obj.get("presentation_proposal_dict") is not None
                    else None
                ),
                "presentation_request": (
                    IndyProofRequest.from_dict(obj["presentation_request"])
                    if obj.get("presentation_request") is not None
                    else None
                ),
                "presentation_request_dict": (
                    PresentationRequest.from_dict(obj["presentation_request_dict"])
                    if obj.get("presentation_request_dict") is not None
                    else None
                ),
                "role": obj.get("role"),
                "state": obj.get("state"),
                "thread_id": obj.get("thread_id"),
                "trace": obj.get("trace"),
                "updated_at": obj.get("updated_at"),
                "verified": obj.get("verified"),
                "verified_msgs": obj.get("verified_msgs"),
            }
        )
        return _obj
