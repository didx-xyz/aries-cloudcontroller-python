# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class GetNymRoleResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetNymRoleResponse - a model defined in OpenAPI
        role: Ledger role [Optional].
    """

    role: Optional[Literal["STEWARD", "TRUSTEE", "ENDORSER", "NETWORK_MONITOR", "USER", "ROLE_REMOVE"]] = None

    def __init__(
        self,
        *,
        role: Optional[Literal["STEWARD", "TRUSTEE", "ENDORSER", "NETWORK_MONITOR", "USER", "ROLE_REMOVE"]] = None,
        **kwargs,
    ):
        super().__init__(
            role=role,
            **kwargs,
        )


GetNymRoleResponse.update_forward_refs()
