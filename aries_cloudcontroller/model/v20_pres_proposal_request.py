# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.v20_pres_proposal_by_format import (
    V20PresProposalByFormat,
)


class V20PresProposalRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresProposalRequest - a model defined in OpenAPI
        connection_id: Connection identifier.
        presentation_proposal: The presentation_proposal of this V20PresProposalRequest.
        auto_present: Whether to respond automatically to presentation requests, building and presenting requested proof [Optional].
        comment: Human-readable comment [Optional].
        trace: Whether to trace event (default false) [Optional].
    """

    connection_id: str
    presentation_proposal: V20PresProposalByFormat
    auto_present: Optional[bool] = None
    comment: Optional[str] = None
    trace: Optional[bool] = None
    model_config = ConfigDict(populate_by_name=True)


V20PresProposalRequest.update_forward_refs()
