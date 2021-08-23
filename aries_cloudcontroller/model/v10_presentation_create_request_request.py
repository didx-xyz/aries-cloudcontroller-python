# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.indy_proof_request import IndyProofRequest


class V10PresentationCreateRequestRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10PresentationCreateRequestRequest - a model defined in OpenAPI
        proof_request: The proof_request of this V10PresentationCreateRequestRequest.
        comment: The comment of this V10PresentationCreateRequestRequest [Optional].
        trace: Whether to trace event (default false) [Optional].
    """

    proof_request: IndyProofRequest
    comment: Optional[str] = None
    trace: Optional[bool] = None

    def __init__(
        self,
        *,
        proof_request: IndyProofRequest,
        comment: Optional[str] = None,
        trace: Optional[bool] = None,
        **kwargs,
    ):
        super().__init__(
            comment=comment,
            proof_request=proof_request,
            trace=trace,
            **kwargs,
        )


V10PresentationCreateRequestRequest.update_forward_refs()
