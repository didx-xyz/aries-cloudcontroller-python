# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator import AttachDecorator
from aries_cloudcontroller.model.credential_preview import CredentialPreview


class CredentialOffer(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredentialOffer - a model defined in OpenAPI
        offersattach: The offersattach of this CredentialOffer.
        id: Message identifier [Optional].
        type: Message type [Optional].
        comment: Human-readable comment [Optional].
        credential_preview: The credential_preview of this CredentialOffer [Optional].
    """

    offersattach: List[AttachDecorator] = Field(..., alias="offers~attach")
    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    comment: Optional[str] = None
    credential_preview: Optional[CredentialPreview] = None
    model_config = ConfigDict(populate_by_name=True)


CredentialOffer.update_forward_refs()
