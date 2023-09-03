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

from aries_cloudcontroller.model.keylist_update_rule import KeylistUpdateRule


class KeylistUpdate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    KeylistUpdate - a model defined in OpenAPI
        id: Message identifier [Optional].
        type: Message type [Optional].
        updates: List of update rules [Optional].
    """

    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    updates: Optional[List[KeylistUpdateRule]] = None
    model_config = ConfigDict(populate_by_name=True)


KeylistUpdate.model_rebuild()
