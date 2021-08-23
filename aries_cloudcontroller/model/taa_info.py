# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.aml_record import AMLRecord
from aries_cloudcontroller.model.taa_acceptance import TAAAcceptance
from aries_cloudcontroller.model.taa_record import TAARecord


class TAAInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TAAInfo - a model defined in OpenAPI
        aml_record: The aml_record of this TAAInfo [Optional].
        taa_accepted: The taa_accepted of this TAAInfo [Optional].
        taa_record: The taa_record of this TAAInfo [Optional].
        taa_required: The taa_required of this TAAInfo [Optional].
    """

    aml_record: Optional[AMLRecord] = None
    taa_accepted: Optional[TAAAcceptance] = None
    taa_record: Optional[TAARecord] = None
    taa_required: Optional[bool] = None

    def __init__(
        self,
        *,
        aml_record: Optional[AMLRecord] = None,
        taa_accepted: Optional[TAAAcceptance] = None,
        taa_record: Optional[TAARecord] = None,
        taa_required: Optional[bool] = None,
        **kwargs,
    ):
        super().__init__(
            aml_record=aml_record,
            taa_accepted=taa_accepted,
            taa_record=taa_record,
            taa_required=taa_required,
            **kwargs,
        )


TAAInfo.update_forward_refs()
