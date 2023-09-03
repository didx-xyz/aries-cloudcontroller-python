# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator import AttachDecorator
from aries_cloudcontroller.model.v20_cred_format import V20CredFormat
from aries_cloudcontroller.model.v20_cred_preview import V20CredPreview


class V20CredOffer(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredOffer - a model defined in OpenAPI
        formats: Acceptable credential formats.
        offersattach: Offer attachments.
        id: Message identifier [Optional].
        type: Message type [Optional].
        comment: Human-readable comment [Optional].
        credential_preview: The credential_preview of this V20CredOffer [Optional].
        replacement_id: Issuer-unique identifier to coordinate credential replacement [Optional].
    """

    formats: List[V20CredFormat]
    offersattach: List[AttachDecorator] = Field(..., alias="offers~attach")
    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    comment: Optional[str] = None
    credential_preview: Optional[V20CredPreview] = None
    replacement_id: Optional[str] = None
    model_config = ConfigDict(populate_by_name=True)


V20CredOffer.update_forward_refs()
