# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.dif_pres_spec import DIFPresSpec
from aries_cloudcontroller.model.indy_pres_spec import IndyPresSpec


class V20PresSpecByFormatRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresSpecByFormatRequest - a model defined in OpenAPI
        dif: Optional Presentation specification for DIF, overrides the PresentionExchange record&#39;s PresRequest [Optional].
        indy: Presentation specification for indy [Optional].
        trace: Record trace information, based on agent configuration [Optional].
    """

    dif: Optional[DIFPresSpec] = None
    indy: Optional[IndyPresSpec] = None
    trace: Optional[bool] = None

    def __init__(
        self,
        *,
        dif: Optional[DIFPresSpec] = None,
        indy: Optional[IndyPresSpec] = None,
        trace: Optional[bool] = None,
        **kwargs,
    ):
        super().__init__(
            dif=dif,
            indy=indy,
            trace=trace,
            **kwargs,
        )


V20PresSpecByFormatRequest.update_forward_refs()
