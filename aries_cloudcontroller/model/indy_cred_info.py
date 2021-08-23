# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class IndyCredInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyCredInfo - a model defined in OpenAPI
        attrs: Attribute names and value [Optional].
        cred_def_id: Credential definition identifier [Optional].
        cred_rev_id: Credential revocation identifier [Optional].
        referent: Wallet referent [Optional].
        rev_reg_id: Revocation registry identifier [Optional].
        schema_id: Schema identifier [Optional].
    """

    attrs: Optional[Dict[str, str]] = None
    cred_def_id: Optional[str] = None
    cred_rev_id: Optional[str] = None
    referent: Optional[str] = None
    rev_reg_id: Optional[str] = None
    schema_id: Optional[str] = None

    def __init__(
        self,
        *,
        attrs: Optional[Dict[str, str]] = None,
        cred_def_id: Optional[str] = None,
        cred_rev_id: Optional[str] = None,
        referent: Optional[str] = None,
        rev_reg_id: Optional[str] = None,
        schema_id: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            attrs=attrs,
            cred_def_id=cred_def_id,
            cred_rev_id=cred_rev_id,
            referent=referent,
            rev_reg_id=rev_reg_id,
            schema_id=schema_id,
            **kwargs,
        )

    @validator("cred_def_id")
    def cred_def_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of cred_def_id does not match regex pattern ('{pattern}')")
        return value

    @validator("cred_rev_id")
    def cred_rev_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[1-9][0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of cred_rev_id does not match regex pattern ('{pattern}')")
        return value

    @validator("rev_reg_id")
    def rev_reg_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"
        if not re.match(pattern, value):
            raise ValueError(f"Value of rev_reg_id does not match regex pattern ('{pattern}')")
        return value

    @validator("schema_id")
    def schema_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of schema_id does not match regex pattern ('{pattern}')")
        return value


IndyCredInfo.update_forward_refs()
