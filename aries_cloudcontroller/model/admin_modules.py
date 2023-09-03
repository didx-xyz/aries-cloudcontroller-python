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


class AdminModules(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AdminModules - a model defined in OpenAPI
        result: List of admin modules [Optional].
    """

    result: Optional[List[str]] = None
    model_config = ConfigDict(populate_by_name=True)


AdminModules.model_rebuild()
