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


class V10CredentialIssueRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10CredentialIssueRequest - a model defined in OpenAPI
        comment: Human-readable comment [Optional].
    """

    comment: Optional[str] = None
    model_config = ConfigDict(populate_by_name=True)


V10CredentialIssueRequest.model_rebuild()
