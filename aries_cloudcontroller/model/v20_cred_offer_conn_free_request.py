# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.v20_cred_filter import V20CredFilter
from aries_cloudcontroller.model.v20_cred_preview import V20CredPreview


class V20CredOfferConnFreeRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredOfferConnFreeRequest - a model defined in OpenAPI
        filter: Credential specification criteria by format.
        auto_issue: Whether to respond automatically to credential requests, creating and issuing requested credentials [Optional].
        auto_remove: Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting) [Optional].
        comment: Human-readable comment [Optional].
        credential_preview: The credential_preview of this V20CredOfferConnFreeRequest [Optional].
        replacement_id: Optional identifier used to manage credential replacement [Optional].
        trace: Record trace information, based on agent configuration [Optional].
    """

    filter: V20CredFilter
    auto_issue: Optional[bool] = None
    auto_remove: Optional[bool] = None
    comment: Optional[str] = None
    credential_preview: Optional[V20CredPreview] = None
    replacement_id: Optional[str] = None
    trace: Optional[bool] = None

    class Config:
        allow_population_by_field_name = True


V20CredOfferConnFreeRequest.update_forward_refs()
