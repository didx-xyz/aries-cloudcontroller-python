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

from aries_cloudcontroller.model.generated import Generated


class CredDefValuePrimary(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredDefValuePrimary - a model defined in OpenAPI
        n: The n of this CredDefValuePrimary [Optional].
        r: The r of this CredDefValuePrimary [Optional].
        rctxt: The rctxt of this CredDefValuePrimary [Optional].
        s: The s of this CredDefValuePrimary [Optional].
        z: The z of this CredDefValuePrimary [Optional].
    """

    n: Optional[str] = None
    r: Optional[Generated] = None
    rctxt: Optional[str] = None
    s: Optional[str] = None
    z: Optional[str] = None

    @field_validator("n")
    @classmethod
    def n_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of n does not match regex pattern ('{pattern}')")
        return value

    @field_validator("rctxt")
    @classmethod
    def rctxt_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of rctxt does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("s")
    @classmethod
    def s_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of s does not match regex pattern ('{pattern}')")
        return value

    @field_validator("z")
    @classmethod
    def z_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of z does not match regex pattern ('{pattern}')")
        return value

    model_config = ConfigDict(populate_by_name=True)


CredDefValuePrimary.model_rebuild()
