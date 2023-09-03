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


class IndyNonRevocProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyNonRevocProof - a model defined in OpenAPI
        c_list: The c_list of this IndyNonRevocProof [Optional].
        x_list: The x_list of this IndyNonRevocProof [Optional].
    """

    c_list: Optional[Dict[str, str]] = None
    x_list: Optional[Dict[str, str]] = None
    model_config = ConfigDict(populate_by_name=True)


IndyNonRevocProof.model_rebuild()
