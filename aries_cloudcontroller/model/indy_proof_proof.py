# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.indy_proof_proof_aggregated_proof import (
    IndyProofProofAggregatedProof,
)
from aries_cloudcontroller.model.indy_proof_proof_proofs_proof import (
    IndyProofProofProofsProof,
)


class IndyProofProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofProof - a model defined in OpenAPI
        aggregated_proof: Indy proof aggregated proof [Optional].
        proofs: Indy proof proofs [Optional].
    """

    aggregated_proof: Optional[IndyProofProofAggregatedProof] = None
    proofs: Optional[List[IndyProofProofProofsProof]] = None

    def __init__(
        self,
        *,
        aggregated_proof: Optional[IndyProofProofAggregatedProof] = None,
        proofs: Optional[List[IndyProofProofProofsProof]] = None,
        **kwargs,
    ):
        super().__init__(
            aggregated_proof=aggregated_proof,
            proofs=proofs,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


IndyProofProof.update_forward_refs()