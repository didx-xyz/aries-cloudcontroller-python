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


class TAARecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TAARecord - a model defined in OpenAPI
        digest: The digest of this TAARecord [Optional].
        text: The text of this TAARecord [Optional].
        version: The version of this TAARecord [Optional].
    """

    digest: Optional[str] = None
    text: Optional[str] = None
    version: Optional[str] = None
    model_config = ConfigDict(populate_by_name=True)


TAARecord.model_rebuild()
