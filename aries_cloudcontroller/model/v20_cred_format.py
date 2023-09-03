# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class V20CredFormat(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredFormat - a model defined in OpenAPI
        attach_id: Attachment identifier.
        format: Attachment format specifier.
    """

    attach_id: str
    format: str
    model_config = ConfigDict(populate_by_name=True)


V20CredFormat.model_rebuild()
