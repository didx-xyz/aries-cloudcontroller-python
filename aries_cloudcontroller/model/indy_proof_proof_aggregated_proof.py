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


class IndyProofProofAggregatedProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofProofAggregatedProof - a model defined in OpenAPI
        c_hash: c_hash value [Optional].
        c_list: c_list value [Optional].
    """

    c_hash: Optional[str] = None
    c_list: Optional[List[List[int]]] = None
    model_config = ConfigDict(populate_by_name=True)


IndyProofProofAggregatedProof.model_rebuild()
