# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.ld_proof_vc_detail import LDProofVCDetail
from aries_cloudcontroller.model.v20_cred_filter_indy import V20CredFilterIndy


class V20CredFilter(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredFilter - a model defined in OpenAPI
        indy: Credential filter for indy [Optional].
        ld_proof: Credential filter for linked data proof [Optional].
    """

    indy: Optional[V20CredFilterIndy] = None
    ld_proof: Optional[LDProofVCDetail] = None
    model_config = ConfigDict(populate_by_name=True)


V20CredFilter.model_rebuild()
