# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class MediationIdMatchInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MediationIdMatchInfo - a model defined in OpenAPI
        mediation_id: Mediation record identifier [Optional].
    """

    mediation_id: Optional[str] = None
    model_config = ConfigDict(populate_by_name=True)


MediationIdMatchInfo.update_forward_refs()
