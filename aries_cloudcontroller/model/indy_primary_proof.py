# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.indy_eq_proof import IndyEQProof
from aries_cloudcontroller.model.indy_ge_proof import IndyGEProof


class IndyPrimaryProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyPrimaryProof - a model defined in OpenAPI
        eq_proof: Indy equality proof [Optional].
        ge_proofs: Indy GE proofs [Optional].
    """

    eq_proof: Optional[IndyEQProof] = None
    ge_proofs: Optional[List[IndyGEProof]] = None
    model_config = ConfigDict(populate_by_name=True)


IndyPrimaryProof.update_forward_refs()
