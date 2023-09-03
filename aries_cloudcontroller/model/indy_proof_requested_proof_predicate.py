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


class IndyProofRequestedProofPredicate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofRequestedProofPredicate - a model defined in OpenAPI
        sub_proof_index: Sub-proof index [Optional].
    """

    sub_proof_index: Optional[int] = None
    model_config = ConfigDict(populate_by_name=True)


IndyProofRequestedProofPredicate.model_rebuild()
