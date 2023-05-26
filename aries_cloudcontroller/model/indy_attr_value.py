# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class IndyAttrValue(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyAttrValue - a model defined in OpenAPI
        encoded: Attribute encoded value.
        raw: Attribute raw value.
    """

    encoded: str
    raw: str

    @validator("encoded")
    def encoded_pattern(cls, value):
        pattern = r"^-?[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of encoded does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


IndyAttrValue.update_forward_refs()
