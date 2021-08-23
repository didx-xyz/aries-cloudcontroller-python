# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class ClearPendingRevocationsRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ClearPendingRevocationsRequest - a model defined in OpenAPI
        purge: Credential revocation ids by revocation registry id: omit for all, specify null or empty list for all pending per revocation registry [Optional].
    """

    purge: Optional[Dict[str, List[str]]] = None

    def __init__(
        self,
        *,
        purge: Optional[Dict[str, List[str]]] = None,
        **kwargs,
    ):
        super().__init__(
            purge=purge,
            **kwargs,
        )


ClearPendingRevocationsRequest.update_forward_refs()
