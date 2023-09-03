# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.issuer_rev_reg_record import IssuerRevRegRecord


class RevRegResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RevRegResult - a model defined in OpenAPI
        result: The result of this RevRegResult [Optional].
    """

    result: Optional[IssuerRevRegRecord] = None
    model_config = ConfigDict(populate_by_name=True)


RevRegResult.model_rebuild()
