# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.v20_cred_ex_record_by_format import V20CredExRecordByFormat
from aries_cloudcontroller.model.v20_cred_issue import V20CredIssue
from aries_cloudcontroller.model.v20_cred_offer import V20CredOffer
from aries_cloudcontroller.model.v20_cred_preview import V20CredPreview
from aries_cloudcontroller.model.v20_cred_proposal import V20CredProposal
from aries_cloudcontroller.model.v20_cred_request import V20CredRequest


class V20CredExRecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredExRecord - a model defined in OpenAPI
        auto_issue: Issuer choice to issue to request in this credential exchange [Optional].
        auto_offer: Holder choice to accept offer in this credential exchange [Optional].
        auto_remove: Issuer choice to remove this credential exchange record when complete [Optional].
        by_format: Attachment content by format for proposal, offer, request, and issue [Optional].
        connection_id: Connection identifier [Optional].
        created_at: Time of record creation [Optional].
        cred_ex_id: Credential exchange identifier [Optional].
        cred_issue: Serialized credential issue message [Optional].
        cred_offer: Credential offer message [Optional].
        cred_preview: Credential preview from credential proposal [Optional].
        cred_proposal: Credential proposal message [Optional].
        cred_request: Serialized credential request message [Optional].
        error_msg: Error message [Optional].
        initiator: Issue-credential exchange initiator: self or external [Optional].
        parent_thread_id: Parent thread identifier [Optional].
        role: Issue-credential exchange role: holder or issuer [Optional].
        state: Issue-credential exchange state [Optional].
        thread_id: Thread identifier [Optional].
        trace: Record trace information, based on agent configuration [Optional].
        updated_at: Time of last record update [Optional].
    """

    auto_issue: Optional[bool] = None
    auto_offer: Optional[bool] = None
    auto_remove: Optional[bool] = None
    by_format: Optional[V20CredExRecordByFormat] = None
    connection_id: Optional[str] = None
    created_at: Optional[str] = None
    cred_ex_id: Optional[str] = None
    cred_issue: Optional[V20CredIssue] = None
    cred_offer: Optional[V20CredOffer] = None
    cred_preview: Optional[V20CredPreview] = None
    cred_proposal: Optional[V20CredProposal] = None
    cred_request: Optional[V20CredRequest] = None
    error_msg: Optional[str] = None
    initiator: Optional[Literal["self", "external"]] = None
    parent_thread_id: Optional[str] = None
    role: Optional[Literal["issuer", "holder"]] = None
    state: Optional[Literal["proposal-sent", "proposal-received", "offer-sent", "offer-received", "request-sent", "request-received", "credential-issued", "credential-received", "done"]] = None
    thread_id: Optional[str] = None
    trace: Optional[bool] = None
    updated_at: Optional[str] = None

    def __init__(
        self,
        *,
        auto_issue: Optional[bool] = None,
        auto_offer: Optional[bool] = None,
        auto_remove: Optional[bool] = None,
        by_format: Optional[V20CredExRecordByFormat] = None,
        connection_id: Optional[str] = None,
        created_at: Optional[str] = None,
        cred_ex_id: Optional[str] = None,
        cred_issue: Optional[V20CredIssue] = None,
        cred_offer: Optional[V20CredOffer] = None,
        cred_preview: Optional[V20CredPreview] = None,
        cred_proposal: Optional[V20CredProposal] = None,
        cred_request: Optional[V20CredRequest] = None,
        error_msg: Optional[str] = None,
        initiator: Optional[Literal["self", "external"]] = None,
        parent_thread_id: Optional[str] = None,
        role: Optional[Literal["issuer", "holder"]] = None,
        state: Optional[Literal["proposal-sent", "proposal-received", "offer-sent", "offer-received", "request-sent", "request-received", "credential-issued", "credential-received", "done"]] = None,
        thread_id: Optional[str] = None,
        trace: Optional[bool] = None,
        updated_at: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            auto_issue=auto_issue,
            auto_offer=auto_offer,
            auto_remove=auto_remove,
            by_format=by_format,
            connection_id=connection_id,
            created_at=created_at,
            cred_ex_id=cred_ex_id,
            cred_issue=cred_issue,
            cred_offer=cred_offer,
            cred_preview=cred_preview,
            cred_proposal=cred_proposal,
            cred_request=cred_request,
            error_msg=error_msg,
            initiator=initiator,
            parent_thread_id=parent_thread_id,
            role=role,
            state=state,
            thread_id=thread_id,
            trace=trace,
            updated_at=updated_at,
            **kwargs,
        )

    @validator("created_at")
    def created_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of created_at does not match regex pattern ('{pattern}')")
        return value

    @validator("updated_at")
    def updated_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of updated_at does not match regex pattern ('{pattern}')")
        return value


V20CredExRecord.update_forward_refs()
