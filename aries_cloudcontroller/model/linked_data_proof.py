# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import (
    field_validator,
    ConfigDict,
    AnyUrl,
    BaseModel,
    EmailStr,
    Field,
    Extra,
)  # noqa: F401


class LinkedDataProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LinkedDataProof - a model defined in OpenAPI
        created: The string value of an ISO8601 combined date and time string generated by the Signature Algorithm.
        proof_purpose: Proof purpose.
        type: Identifies the digital signature suite that was used to create the signature.
        verification_method: Information used for proof verification.
        challenge: Associates a challenge with a proof, for use with a proofPurpose such as authentication [Optional].
        domain: A string value specifying the restricted domain of the signature. [Optional].
        jws: Associates a Detached Json Web Signature with a proof [Optional].
        nonce: The nonce [Optional].
        proof_value: The proof value of a proof [Optional].
    """

    created: str
    proof_purpose: str = Field(..., alias="proofPurpose")
    type: str
    verification_method: str = Field(..., alias="verificationMethod")
    challenge: Optional[str] = None
    domain: Optional[str] = None
    jws: Optional[str] = None
    nonce: Optional[str] = None
    proof_value: Optional[str] = Field(None, alias="proofValue")

    @field_validator("created")
    @classmethod
    def created_pattern(cls, value):
        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of created does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("domain")
    @classmethod
    def domain_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"\w+:(\\/?\\/?)[^\s]+"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of domain does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("verification_method")
    @classmethod
    def verification_method_pattern(cls, value):
        pattern = r"\w+:(\\/?\\/?)[^\s]+"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of verification_method does not match regex pattern ('{pattern}')"
            )
        return value

    model_config = ConfigDict(populate_by_name=True)


LinkedDataProof.model_rebuild()
