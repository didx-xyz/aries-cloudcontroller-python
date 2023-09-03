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


class IndyKeyCorrectnessProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyKeyCorrectnessProof - a model defined in OpenAPI
        c: c in key correctness proof.
        xr_cap: xr_cap in key correctness proof.
        xz_cap: xz_cap in key correctness proof.
    """

    c: str
    xr_cap: List[List[str]]
    xz_cap: str

    @field_validator("c")
    @classmethod
    def c_pattern(cls, value):
        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of c does not match regex pattern ('{pattern}')")
        return value

    @field_validator("xz_cap")
    @classmethod
    def xz_cap_pattern(cls, value):
        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of xz_cap does not match regex pattern ('{pattern}')"
            )
        return value

    model_config = ConfigDict(populate_by_name=True)


IndyKeyCorrectnessProof.model_rebuild()
