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

from aries_cloudcontroller.model.v20_cred_filter import V20CredFilter
from aries_cloudcontroller.model.v20_cred_preview import V20CredPreview


class V20CredExFree(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredExFree - a model defined in OpenAPI
        connection_id: Connection identifier.
        filter: Credential specification criteria by format.
        auto_remove: Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting) [Optional].
        comment: Human-readable comment [Optional].
        credential_preview: The credential_preview of this V20CredExFree [Optional].
        replacement_id: Optional identifier used to manage credential replacement [Optional].
        trace: Record trace information, based on agent configuration [Optional].
        verification_method: For ld-proofs. Verification method for signing. [Optional].
    """

    connection_id: str
    filter: V20CredFilter
    auto_remove: Optional[bool] = None
    comment: Optional[str] = None
    credential_preview: Optional[V20CredPreview] = None
    replacement_id: Optional[str] = None
    trace: Optional[bool] = None
    verification_method: Optional[str] = None
    model_config = ConfigDict(populate_by_name=True)


V20CredExFree.model_rebuild()
