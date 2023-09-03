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


class JWSVerify(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    JWSVerify - a model defined in OpenAPI
        jwt: The jwt of this JWSVerify [Optional].
    """

    jwt: Optional[str] = None

    @field_validator("jwt")
    @classmethod
    def jwt_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[-_a-zA-Z0-9]*\.[-_a-zA-Z0-9]*\.[-_a-zA-Z0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of jwt does not match regex pattern ('{pattern}')")
        return value

    model_config = ConfigDict(populate_by_name=True)


JWSVerify.model_rebuild()
