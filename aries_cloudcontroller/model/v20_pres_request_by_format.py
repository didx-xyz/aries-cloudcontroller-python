# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Literal, Optional, Union  # noqa: F401

from pydantic import (  # noqa: F401
    AnyUrl,
    BaseModel,
    ConfigDict,
    EmailStr,
    Extra,
    Field,
    validator,
)

from aries_cloudcontroller.model.dif_proof_request import DIFProofRequest
from aries_cloudcontroller.model.indy_proof_request import IndyProofRequest


class V20PresRequestByFormat(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresRequestByFormat - a model defined in OpenAPI
        dif: Presentation request for DIF [Optional].
        indy: Presentation request for indy [Optional].
    """

    dif: Optional[DIFProofRequest] = None
    indy: Optional[IndyProofRequest] = None
    model_config = ConfigDict(populate_by_name=True)


V20PresRequestByFormat.model_rebuild()
