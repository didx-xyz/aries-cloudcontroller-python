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


class ClaimFormat(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ClaimFormat - a model defined in OpenAPI
        jwt: The jwt of this ClaimFormat [Optional].
        jwt_vc: The jwt_vc of this ClaimFormat [Optional].
        jwt_vp: The jwt_vp of this ClaimFormat [Optional].
        ldp: The ldp of this ClaimFormat [Optional].
        ldp_vc: The ldp_vc of this ClaimFormat [Optional].
        ldp_vp: The ldp_vp of this ClaimFormat [Optional].
    """

    jwt: Optional[Dict[str, Any]] = None
    jwt_vc: Optional[Dict[str, Any]] = None
    jwt_vp: Optional[Dict[str, Any]] = None
    ldp: Optional[Dict[str, Any]] = None
    ldp_vc: Optional[Dict[str, Any]] = None
    ldp_vp: Optional[Dict[str, Any]] = None
    model_config = ConfigDict(populate_by_name=True)


ClaimFormat.model_rebuild()
