# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field, Extra  # noqa: F401


class RevRegIssuedResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RevRegIssuedResult - a model defined in OpenAPI
        result: Number of credentials issued against revocation registry [Optional].
    """

    result: Optional[int] = None

    @field_validator("result")
    @classmethod
    def result_min(cls, value):
        # Property is optional
        if value is None:
            return

        if value < 0:
            raise ValueError(f"result must be greater than 0, currently {value}")
        return value
    model_config = ConfigDict(populate_by_name=True)


RevRegIssuedResult.update_forward_refs()
