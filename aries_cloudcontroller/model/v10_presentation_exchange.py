# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
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

    def __init__(
        self,
        *,
        auto_present: Optional[bool] = None,
        auto_verify: Optional[bool] = None,
        connection_id: Optional[str] = None,
        created_at: Optional[str] = None,
        error_msg: Optional[str] = None,
        initiator: Optional[Literal["self", "external"]] = None,
        presentation: Optional[IndyProof] = None,
        presentation_exchange_id: Optional[str] = None,
        presentation_proposal_dict: Optional[PresentationProposal] = None,
        presentation_request: Optional[IndyProofRequest] = None,
        presentation_request_dict: Optional[PresentationRequest] = None,
        role: Optional[Literal["prover", "verifier"]] = None,
        state: Optional[str] = None,
        thread_id: Optional[str] = None,
        trace: Optional[bool] = None,
        updated_at: Optional[str] = None,
        verified: Optional[Literal["true", "false"]] = None,
        verified_msgs: Optional[List[str]] = None,
        **kwargs,
    ):
        # Manually handle the alias of `request_presentationsattach` in `PresentationRequest`
        if presentation_request_dict:
            if (
                isinstance(presentation_request_dict, dict)
                and "request_presentations~attach" in presentation_request_dict
            ):
                presentation_request_dict[
                    "request_presentationsattach"
                ] = presentation_request_dict.pop("request_presentations~attach")

        super().__init__(
            auto_present=auto_present,
            auto_verify=auto_verify,
            connection_id=connection_id,
            created_at=created_at,
            error_msg=error_msg,
            initiator=initiator,
            presentation=presentation,
            presentation_exchange_id=presentation_exchange_id,
            presentation_proposal_dict=presentation_proposal_dict,
            presentation_request=presentation_request,
            presentation_request_dict=presentation_request_dict,
            role=role,
            state=state,
            thread_id=thread_id,
            trace=trace,
            updated_at=updated_at,
            verified=verified,
            verified_msgs=verified_msgs,
            **kwargs,
        )

    @validator("created_at")
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

    @validator("updated_at")
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

    class Config:
        allow_population_by_field_name = True


V10PresentationExchange.update_forward_refs()
