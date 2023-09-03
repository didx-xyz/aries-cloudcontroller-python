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


class TAAAcceptance(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TAAAcceptance - a model defined in OpenAPI
        mechanism: The mechanism of this TAAAcceptance [Optional].
        time: The time of this TAAAcceptance [Optional].
    """

    mechanism: Optional[str] = None
    time: Optional[int] = None

    @field_validator("time")
    @classmethod
    def time_max(cls, value):
        # Property is optional
        if value is None:
            return

        if value > 18446744073709551615:
            raise ValueError(
                f"time must be less than 18446744073709551615, currently {value}"
            )
        return value

    @field_validator("time")
    @classmethod
    def time_min(cls, value):
        # Property is optional
        if value is None:
            return

        if value < 0:
            raise ValueError(f"time must be greater than 0, currently {value}")
        return value

    model_config = ConfigDict(populate_by_name=True)


TAAAcceptance.model_rebuild()
