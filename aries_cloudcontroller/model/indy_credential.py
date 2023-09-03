# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.indy_attr_value import IndyAttrValue


class IndyCredential(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyCredential - a model defined in OpenAPI
        cred_def_id: Credential definition identifier.
        schema_id: Schema identifier.
        signature: Credential signature.
        signature_correctness_proof: Credential signature correctness proof.
        values: Credential attributes.
        rev_reg: Revocation registry state [Optional].
        rev_reg_id: Revocation registry identifier [Optional].
        witness: Witness for revocation proof [Optional].
    """

    cred_def_id: str
    schema_id: str
    signature: Dict[str, Any]
    signature_correctness_proof: Dict[str, Any]
    values: Dict[str, IndyAttrValue]
    rev_reg: Optional[Dict[str, Any]] = None
    rev_reg_id: Optional[str] = None
    witness: Optional[Dict[str, Any]] = None

    @field_validator("cred_def_id")
    @classmethod
    def cred_def_id_pattern(cls, value):
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
        pattern = r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_id does not match regex pattern ('{pattern}')"
            )
        return value
    model_config = ConfigDict(populate_by_name=True)


IndyCredential.model_rebuild()
