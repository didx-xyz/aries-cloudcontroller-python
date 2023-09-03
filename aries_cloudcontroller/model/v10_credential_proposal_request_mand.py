# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.credential_preview import CredentialPreview


class V10CredentialProposalRequestMand(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10CredentialProposalRequestMand - a model defined in OpenAPI
        connection_id: Connection identifier.
        credential_proposal: The credential_proposal of this V10CredentialProposalRequestMand.
        auto_remove: Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting) [Optional].
        comment: Human-readable comment [Optional].
        cred_def_id: Credential definition identifier [Optional].
        issuer_did: Credential issuer DID [Optional].
        schema_id: Schema identifier [Optional].
        schema_issuer_did: Schema issuer DID [Optional].
        schema_name: Schema name [Optional].
        schema_version: Schema version [Optional].
        trace: Record trace information, based on agent configuration [Optional].
    """

    connection_id: str
    credential_proposal: CredentialPreview
    auto_remove: Optional[bool] = None
    comment: Optional[str] = None
    cred_def_id: Optional[str] = None
    issuer_did: Optional[str] = None
    schema_id: Optional[str] = None
    schema_issuer_did: Optional[str] = None
    schema_name: Optional[str] = None
    schema_version: Optional[str] = None
    trace: Optional[bool] = None

    @field_validator("cred_def_id")
    @classmethod
    def cred_def_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of cred_def_id does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("issuer_did")
    @classmethod
    def issuer_did_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of issuer_did does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("schema_id")
    @classmethod
    def schema_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_id does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("schema_issuer_did")
    @classmethod
    def schema_issuer_did_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_issuer_did does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("schema_version")
    @classmethod
    def schema_version_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_version does not match regex pattern ('{pattern}')"
            )
        return value
    model_config = ConfigDict(populate_by_name=True)


V10CredentialProposalRequestMand.model_rebuild()
