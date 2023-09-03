# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field, Extra  # noqa: F401


class IndyPresAttrSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyPresAttrSpec - a model defined in OpenAPI
        name: Attribute name.
        cred_def_id: The cred_def_id of this IndyPresAttrSpec [Optional].
        mime_type: MIME type (default null) [Optional].
        referent: Credential referent [Optional].
        value: Attribute value [Optional].
    """

    name: str
    cred_def_id: Optional[str] = None
    mime_type: Optional[str] = Field(None, alias="mime-type")
    referent: Optional[str] = None
    value: Optional[str] = None

    @field_validator("cred_def_id")
    @classmethod
    def cred_def_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of cred_def_id does not match regex pattern ('{pattern}')"
            )
        return value
    model_config = ConfigDict(populate_by_name=True)


IndyPresAttrSpec.update_forward_refs()
