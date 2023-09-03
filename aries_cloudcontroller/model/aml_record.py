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


class AMLRecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AMLRecord - a model defined in OpenAPI
        aml: The aml of this AMLRecord [Optional].
        aml_context: The aml_context of this AMLRecord [Optional].
        version: The version of this AMLRecord [Optional].
    """

    aml: Optional[Dict[str, str]] = None
    aml_context: Optional[str] = Field(None, alias="amlContext")
    version: Optional[str] = None
    model_config = ConfigDict(populate_by_name=True)


AMLRecord.model_rebuild()
