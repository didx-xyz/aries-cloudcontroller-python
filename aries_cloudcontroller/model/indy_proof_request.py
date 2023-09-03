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
    field_validator,
)

from aries_cloudcontroller.model.indy_proof_req_attr_spec import IndyProofReqAttrSpec
from aries_cloudcontroller.model.indy_proof_req_pred_spec import IndyProofReqPredSpec
from aries_cloudcontroller.model.indy_proof_request_non_revoked import (
    IndyProofRequestNonRevoked,
)


class IndyProofRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofRequest - a model defined in OpenAPI
        requested_attributes: Requested attribute specifications of proof request.
        requested_predicates: Requested predicate specifications of proof request.
        name: Proof request name [Optional].
        non_revoked: The non_revoked of this IndyProofRequest [Optional].
        nonce: Nonce [Optional].
        version: Proof request version [Optional].
    """

    requested_attributes: Dict[str, IndyProofReqAttrSpec]
    requested_predicates: Dict[str, IndyProofReqPredSpec]
    name: Optional[str] = None
    non_revoked: Optional[IndyProofRequestNonRevoked] = None
    nonce: Optional[str] = None
    version: Optional[str] = None

    @field_validator("nonce")
    @classmethod
    def nonce_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[1-9][0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of nonce does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("version")
    @classmethod
    def version_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of version does not match regex pattern ('{pattern}')"
            )
        return value

    model_config = ConfigDict(populate_by_name=True)


IndyProofRequest.model_rebuild()
