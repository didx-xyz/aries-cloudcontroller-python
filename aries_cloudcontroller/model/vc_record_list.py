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
from aries_cloudcontroller.model.vc_record import VCRecord


class VCRecordList(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    VCRecordList - a model defined in OpenAPI
        results: The results of this VCRecordList [Optional].
    """

    results: Optional[List[VCRecord]] = None
    model_config = ConfigDict(populate_by_name=True)


VCRecordList.model_rebuild()
