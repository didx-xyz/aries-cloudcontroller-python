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


class ConnectionStaticRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ConnectionStaticRequest - a model defined in OpenAPI
        alias: Alias to assign to this connection [Optional].
        my_did: Local DID [Optional].
        my_seed: Seed to use for the local DID [Optional].
        their_did: Remote DID [Optional].
        their_endpoint: URL endpoint for other party [Optional].
        their_label: Other party&#39;s label for this connection [Optional].
        their_seed: Seed to use for the remote DID [Optional].
        their_verkey: Remote verification key [Optional].
    """

    alias: Optional[str] = None
    my_did: Optional[str] = None
    my_seed: Optional[str] = None
    their_did: Optional[str] = None
    their_endpoint: Optional[str] = None
    their_label: Optional[str] = None
    their_seed: Optional[str] = None
    their_verkey: Optional[str] = None

    @field_validator("my_did")
    @classmethod
    def my_did_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of my_did does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("their_did")
    @classmethod
    def their_did_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of their_did does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("their_endpoint")
    @classmethod
    def their_endpoint_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of their_endpoint does not match regex pattern ('{pattern}')"
            )
        return value

    model_config = ConfigDict(populate_by_name=True)


ConnectionStaticRequest.model_rebuild()
