# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class PingRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PingRequest - a model defined in OpenAPI
        comment: Comment for the ping message [Optional].
    """

    comment: Optional[str] = None

    def __init__(
        self,
        *,
        comment: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            comment=comment,
            **kwargs,
        )


PingRequest.update_forward_refs()
