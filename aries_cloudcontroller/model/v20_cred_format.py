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


class V20CredFormat(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredFormat - a model defined in OpenAPI
        attach_id: Attachment identifier.
        format: Attachment format specifier.
    """

    attach_id: str
    format: str
    model_config = ConfigDict(populate_by_name=True)


V20CredFormat.model_rebuild()
