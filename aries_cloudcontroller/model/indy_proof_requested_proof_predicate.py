# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class IndyProofRequestedProofPredicate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofRequestedProofPredicate - a model defined in OpenAPI
        sub_proof_index: Sub-proof index [Optional].
    """

    sub_proof_index: Optional[int] = None

    def __init__(
        self,
        *,
        sub_proof_index: Optional[int] = None,
        **kwargs,
    ):
        super().__init__(
            sub_proof_index=sub_proof_index,
            **kwargs,
        )


IndyProofRequestedProofPredicate.update_forward_refs()
