# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class JWSVerifyResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    JWSVerifyResponse - a model defined in OpenAPI
        headers: Headers from verified JWT..
        kid: kid of signer.
        payload: Payload from verified JWT.
        valid: The valid of this JWSVerifyResponse.
        error: Error text [Optional].
    """

    headers: Dict[str, Any]
    kid: str
    payload: Dict[str, Any]
    valid: bool
    error: Optional[str] = None
    model_config = ConfigDict(populate_by_name=True)


JWSVerifyResponse.model_rebuild()
