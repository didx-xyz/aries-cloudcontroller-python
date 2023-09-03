# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class UpdateProfileSettings(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UpdateProfileSettings - a model defined in OpenAPI
        extra_settings: Agent config key-value pairs [Optional].
    """

    extra_settings: Optional[Dict[str, Any]] = None
    model_config = ConfigDict(populate_by_name=True)


UpdateProfileSettings.model_rebuild()
