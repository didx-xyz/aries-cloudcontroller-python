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

from aries_cloudcontroller.model.v20_cred_ex_record import V20CredExRecord
from aries_cloudcontroller.model.v20_cred_ex_record_indy import V20CredExRecordIndy
from aries_cloudcontroller.model.v20_cred_ex_record_ld_proof import (
    V20CredExRecordLDProof,
)


class V20CredExRecordDetail(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredExRecordDetail - a model defined in OpenAPI
        cred_ex_record: Credential exchange record [Optional].
        indy: The indy of this V20CredExRecordDetail [Optional].
        ld_proof: The ld_proof of this V20CredExRecordDetail [Optional].
    """

    cred_ex_record: Optional[V20CredExRecord] = None
    indy: Optional[V20CredExRecordIndy] = None
    ld_proof: Optional[V20CredExRecordLDProof] = None
    model_config = ConfigDict(populate_by_name=True)


V20CredExRecordDetail.model_rebuild()
