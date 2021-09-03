# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class RawEncoded(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RawEncoded - a model defined in OpenAPI
        encoded: Encoded value [Optional].
        raw: Raw value [Optional].
    """

    encoded: Optional[str] = None
    raw: Optional[str] = None

    def __init__(
        self,
        *,
        encoded: Optional[str] = None,
        raw: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            encoded=encoded,
            raw=raw,
            **kwargs,
        )

    @validator("encoded")
    def encoded_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of encoded does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


RawEncoded.update_forward_refs()