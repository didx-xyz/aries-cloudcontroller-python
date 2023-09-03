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


class RevRegWalletUpdatedResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RevRegWalletUpdatedResult - a model defined in OpenAPI
        accum_calculated: Calculated accumulator for phantom revocations [Optional].
        accum_fixed: Applied ledger transaction to fix revocations [Optional].
        rev_reg_delta: Indy revocation registry delta [Optional].
    """

    accum_calculated: Optional[Dict[str, Any]] = None
    accum_fixed: Optional[Dict[str, Any]] = None
    rev_reg_delta: Optional[Dict[str, Any]] = None
    model_config = ConfigDict(populate_by_name=True)


RevRegWalletUpdatedResult.model_rebuild()
