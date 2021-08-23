# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.indy_proof_req_attr_spec_non_revoked import IndyProofReqAttrSpecNonRevoked


class IndyProofReqAttrSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofReqAttrSpec - a model defined in OpenAPI
        name: Attribute name [Optional].
        names: Attribute name group [Optional].
        non_revoked: The non_revoked of this IndyProofReqAttrSpec [Optional].
        restrictions: If present, credential must satisfy one of given restrictions: specify schema_id, schema_issuer_did, schema_name, schema_version, issuer_did, cred_def_id, and/or attr::&lt;attribute-name&gt;::value where &lt;attribute-name&gt; represents a credential attribute name [Optional].
    """

    name: Optional[str] = None
    names: Optional[List[str]] = None
    non_revoked: Optional[IndyProofReqAttrSpecNonRevoked] = None
    restrictions: Optional[List[Dict[str, str]]] = None

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        names: Optional[List[str]] = None,
        non_revoked: Optional[IndyProofReqAttrSpecNonRevoked] = None,
        restrictions: Optional[List[Dict[str, str]]] = None,
        **kwargs,
    ):
        super().__init__(
            name=name,
            names=names,
            non_revoked=non_revoked,
            restrictions=restrictions,
            **kwargs,
        )


IndyProofReqAttrSpec.update_forward_refs()
