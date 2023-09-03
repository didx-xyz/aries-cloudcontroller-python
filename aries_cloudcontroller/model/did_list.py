# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.did import DID


class DIDList(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DIDList - a model defined in OpenAPI
        results: DID list [Optional].
    """

    results: Optional[List[DID]] = None
    model_config = ConfigDict(populate_by_name=True)


DIDList.model_rebuild()
