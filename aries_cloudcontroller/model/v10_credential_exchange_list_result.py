# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import (
    ConfigDict,
    AnyUrl,
    BaseModel,
    EmailStr,
    validator,
    Field,
    Extra,
)  # noqa: F401
from aries_cloudcontroller.model.v10_credential_exchange import V10CredentialExchange


class V10CredentialExchangeListResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10CredentialExchangeListResult - a model defined in OpenAPI
        results: Aries#0036 v1.0 credential exchange records [Optional].
    """

    results: Optional[List[V10CredentialExchange]] = None
    model_config = ConfigDict(populate_by_name=True)


V10CredentialExchangeListResult.model_rebuild()
