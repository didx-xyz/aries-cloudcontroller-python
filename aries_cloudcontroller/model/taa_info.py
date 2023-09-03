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
    model_config = ConfigDict(populate_by_name=True)


TAAInfo.model_rebuild()
