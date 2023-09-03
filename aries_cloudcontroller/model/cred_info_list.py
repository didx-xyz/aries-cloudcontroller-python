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

from aries_cloudcontroller.model.indy_cred_info import IndyCredInfo


class CredInfoList(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredInfoList - a model defined in OpenAPI
        results: The results of this CredInfoList [Optional].
    """

    results: Optional[List[IndyCredInfo]] = None
    model_config = ConfigDict(populate_by_name=True)


CredInfoList.model_rebuild()
