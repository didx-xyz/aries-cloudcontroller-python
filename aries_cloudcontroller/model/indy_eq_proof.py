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


class IndyEQProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyEQProof - a model defined in OpenAPI
        a_prime: The a_prime of this IndyEQProof [Optional].
        e: The e of this IndyEQProof [Optional].
        m: The m of this IndyEQProof [Optional].
        m2: The m2 of this IndyEQProof [Optional].
        revealed_attrs: The revealed_attrs of this IndyEQProof [Optional].
        v: The v of this IndyEQProof [Optional].
    """

    a_prime: Optional[str] = None
    e: Optional[str] = None
    m: Optional[Dict[str, str]] = None
    m2: Optional[str] = None
    revealed_attrs: Optional[Dict[str, str]] = None
    v: Optional[str] = None

    @field_validator("a_prime")
    @classmethod
    def a_prime_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of a_prime does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("e")
    @classmethod
    def e_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of e does not match regex pattern ('{pattern}')")
        return value

    @field_validator("m2")
    @classmethod
    def m2_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of m2 does not match regex pattern ('{pattern}')")
        return value

    @field_validator("v")
    @classmethod
    def v_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of v does not match regex pattern ('{pattern}')")
        return value

    model_config = ConfigDict(populate_by_name=True)


IndyEQProof.model_rebuild()
