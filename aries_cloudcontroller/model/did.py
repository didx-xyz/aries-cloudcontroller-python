# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class DID(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DID - a model defined in OpenAPI
        did: DID of interest [Optional].
        key_type: Key type associated with the DID [Optional].
        method: Did method associated with the DID [Optional].
        posture: Whether DID is current public DID, posted to ledger but not current public DID, or local to the wallet [Optional].
        verkey: Public verification key [Optional].
    """

    did: Optional[str] = None
    key_type: Optional[Literal["ed25519", "bls12381g2"]] = None
    method: Optional[Literal["sov", "key"]] = None
    posture: Optional[Literal["public", "posted", "wallet_only"]] = None
    verkey: Optional[str] = None

    def __init__(
        self,
        *,
        did: Optional[str] = None,
        key_type: Optional[Literal["ed25519", "bls12381g2"]] = None,
        method: Optional[Literal["sov", "key"]] = None,
        posture: Optional[Literal["public", "posted", "wallet_only"]] = None,
        verkey: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            did=did,
            key_type=key_type,
            method=method,
            posture=posture,
            verkey=verkey,
            **kwargs,
        )

    @validator("did")
    def did_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^did:key:z[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]+$|^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of did does not match regex pattern ('{pattern}')")
        return value

    @validator("verkey")
    def verkey_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of verkey does not match regex pattern ('{pattern}')")
        return value


DID.update_forward_refs()
