# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Literal, Optional, Union  # noqa: F401

from pydantic import (  # noqa: F401
    AnyUrl,
    BaseModel,
    ConfigDict,
    EmailStr,
    Extra,
    Field,
    field_validator,
)

from aries_cloudcontroller.model.indy_proof import IndyProof
from aries_cloudcontroller.model.indy_proof_request import IndyProofRequest
from aries_cloudcontroller.model.presentation_proposal import PresentationProposal
from aries_cloudcontroller.model.presentation_request import PresentationRequest


class V10PresentationExchange(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10PresentationExchange - a model defined in OpenAPI
        auto_present: Prover choice to auto-present proof as verifier requests [Optional].
        auto_verify: Verifier choice to auto-verify proof presentation [Optional].
        connection_id: Connection identifier [Optional].
        created_at: Time of record creation [Optional].
        error_msg: Error message [Optional].
        initiator: Present-proof exchange initiator: self or external [Optional].
        presentation: (Indy) presentation (also known as proof) [Optional].
        presentation_exchange_id: Presentation exchange identifier [Optional].
        presentation_proposal_dict: Presentation proposal message [Optional].
        presentation_request: (Indy) presentation request (also known as proof request) [Optional].
        presentation_request_dict: Presentation request message [Optional].
        role: Present-proof exchange role: prover or verifier [Optional].
        state: Present-proof exchange state [Optional].
        thread_id: Thread identifier [Optional].
        trace: Record trace information, based on agent configuration [Optional].
        updated_at: Time of last record update [Optional].
        verified: Whether presentation is verified: true or false [Optional].
        verified_msgs: The verified_msgs of this V10PresentationExchange [Optional].
    """

    auto_present: Optional[bool] = None
    auto_verify: Optional[bool] = None
    connection_id: Optional[str] = None
    created_at: Optional[str] = None
    error_msg: Optional[str] = None
    initiator: Optional[Literal["self", "external"]] = None
    presentation: Optional[IndyProof] = None
    presentation_exchange_id: Optional[str] = None
    presentation_proposal_dict: Optional[PresentationProposal] = None
    presentation_request: Optional[IndyProofRequest] = None
    presentation_request_dict: Optional[PresentationRequest] = None
    role: Optional[Literal["prover", "verifier"]] = None
    state: Optional[str] = None
    thread_id: Optional[str] = None
    trace: Optional[bool] = None
    updated_at: Optional[str] = None
    verified: Optional[Literal["true", "false"]] = None
    verified_msgs: Optional[List[str]] = None

    @field_validator("created_at")
    @classmethod
    def created_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of created_at does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("updated_at")
    @classmethod
    def updated_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of updated_at does not match regex pattern ('{pattern}')"
            )
        return value

    model_config = ConfigDict(populate_by_name=True)


V10PresentationExchange.model_rebuild()
