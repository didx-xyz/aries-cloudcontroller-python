# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class V20CredStoreRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredStoreRequest - a model defined in OpenAPI
        credential_id: The credential_id of this V20CredStoreRequest [Optional].
    """

    credential_id: Optional[str] = None

    def __init__(
        self,
        *,
        credential_id: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            credential_id=credential_id,
            **kwargs,
        )


V20CredStoreRequest.update_forward_refs()
