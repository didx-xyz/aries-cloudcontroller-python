# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.keylist_update_rule import KeylistUpdateRule


class KeylistUpdateRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    KeylistUpdateRequest - a model defined in OpenAPI
        updates: The updates of this KeylistUpdateRequest [Optional].
    """

    updates: Optional[List[KeylistUpdateRule]] = None

    def __init__(
        self,
        *,
        updates: Optional[List[KeylistUpdateRule]] = None,
        **kwargs,
    ):
        super().__init__(
            updates=updates,
            **kwargs,
        )


KeylistUpdateRequest.update_forward_refs()
