# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator_data_jws import AttachDecoratorDataJWS


class AttachDecoratorData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AttachDecoratorData - a model defined in OpenAPI
        base64: Base64-encoded data [Optional].
        json_: JSON-serialized data [Optional].
        jws: Detached Java Web Signature [Optional].
        links: List of hypertext links to data [Optional].
        sha256: SHA256 hash (binhex encoded) of content [Optional].
    """

    base64: Optional[str] = None
    json_: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = Field(
        None, alias="json"
    )
    jws: Optional[AttachDecoratorDataJWS] = None
    links: Optional[List[str]] = None
    sha256: Optional[str] = None

    @field_validator("base64")
    @classmethod
    def base64_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[a-zA-Z0-9+\/]*={0,2}$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of base64 does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("sha256")
    @classmethod
    def sha256_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[a-fA-F0-9+\/]{64}$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of sha256 does not match regex pattern ('{pattern}')"
            )
        return value
    model_config = ConfigDict(populate_by_name=True)


AttachDecoratorData.update_forward_refs()
