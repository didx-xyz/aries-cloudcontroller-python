# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator import AttachDecorator
from aries_cloudcontroller.model.v20_cred_format import V20CredFormat


class V20CredRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredRequest - a model defined in OpenAPI
        formats: Acceptable attachment formats.
        requestsattach: Request attachments.
        id: Message identifier [Optional].
        type: Message type [Optional].
        comment: Human-readable comment [Optional].
    """

    formats: List[V20CredFormat]
    requestsattach: List[AttachDecorator] = Field(..., alias="requests~attach")
    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    comment: Optional[str] = None
    model_config = ConfigDict(populate_by_name=True)


V20CredRequest.update_forward_refs()
