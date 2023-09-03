# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class V20PresentationSendRequestToProposal(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresentationSendRequestToProposal - a model defined in OpenAPI
        auto_verify: Verifier choice to auto-verify proof presentation [Optional].
        trace: Whether to trace event (default false) [Optional].
    """

    auto_verify: Optional[bool] = None
    trace: Optional[bool] = None
    model_config = ConfigDict(populate_by_name=True)


V20PresentationSendRequestToProposal.model_rebuild()
