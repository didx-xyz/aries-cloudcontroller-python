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
    model_config = ConfigDict(populate_by_name=True)


IndyProofProof.model_rebuild()
