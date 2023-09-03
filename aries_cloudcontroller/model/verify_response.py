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
    validator,
)


class VerifyResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    VerifyResponse - a model defined in OpenAPI
        valid: The valid of this VerifyResponse.
        error: Error text [Optional].
    """

    valid: bool
    error: Optional[str] = None
    model_config = ConfigDict(populate_by_name=True)


VerifyResponse.model_rebuild()
