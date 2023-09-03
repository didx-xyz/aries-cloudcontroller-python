# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field, Extra  # noqa: F401


class IndyProofIdentifier(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofIdentifier - a model defined in OpenAPI
        cred_def_id: Credential definition identifier [Optional].
        rev_reg_id: Revocation registry identifier [Optional].
        schema_id: Schema identifier [Optional].
        timestamp: Timestamp epoch [Optional].
    """

    cred_def_id: Optional[str] = None
    rev_reg_id: Optional[str] = None
    schema_id: Optional[str] = None
    timestamp: Optional[int] = None

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

    @field_validator("rev_reg_id")
    @classmethod
    def rev_reg_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of rev_reg_id does not match regex pattern ('{pattern}')"
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

    @field_validator("timestamp")
    @classmethod
    def timestamp_max(cls, value):
        # Property is optional
        if value is None:
            return

        if value > 18446744073709551615:
            raise ValueError(
                f"timestamp must be less than 18446744073709551615, currently {value}"
            )
        return value

    @field_validator("timestamp")
    @classmethod
    def timestamp_min(cls, value):
        # Property is optional
        if value is None:
            return

        if value < 0:
            raise ValueError(f"timestamp must be greater than 0, currently {value}")
        return value
    model_config = ConfigDict(populate_by_name=True)


IndyProofIdentifier.model_rebuild()
