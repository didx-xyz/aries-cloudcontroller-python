# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class ProtocolDescriptor(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ProtocolDescriptor - a model defined in OpenAPI
        pid: The pid of this ProtocolDescriptor.
        roles: List of roles [Optional].
    """

    pid: str
    roles: Optional[List[str]] = None

    def __init__(
        self,
        *,
        pid: str = None,
        roles: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(
            pid=pid,
            roles=roles,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


ProtocolDescriptor.update_forward_refs()
