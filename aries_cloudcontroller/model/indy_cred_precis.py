# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import (
    ConfigDict,
    AnyUrl,
    BaseModel,
    EmailStr,
    validator,
    Field,
    Extra,
)  # noqa: F401
from aries_cloudcontroller.model.indy_cred_info import IndyCredInfo
from aries_cloudcontroller.model.indy_non_revocation_interval import (
    IndyNonRevocationInterval,
)


class IndyCredPrecis(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyCredPrecis - a model defined in OpenAPI
        cred_info: Credential info [Optional].
        interval: Non-revocation interval from presentation request [Optional].
        presentation_referents: The presentation_referents of this IndyCredPrecis [Optional].
    """

    cred_info: Optional[IndyCredInfo] = None
    interval: Optional[IndyNonRevocationInterval] = None
    presentation_referents: Optional[List[str]] = None
    model_config = ConfigDict(populate_by_name=True)


IndyCredPrecis.model_rebuild()
