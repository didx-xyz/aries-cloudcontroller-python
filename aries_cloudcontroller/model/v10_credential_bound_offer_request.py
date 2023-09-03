# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.credential_proposal import CredentialProposal


class V10CredentialBoundOfferRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10CredentialBoundOfferRequest - a model defined in OpenAPI
        counter_proposal: Optional counter-proposal [Optional].
    """

    counter_proposal: Optional[CredentialProposal] = None
    model_config = ConfigDict(populate_by_name=True)


V10CredentialBoundOfferRequest.model_rebuild()
