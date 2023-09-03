# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator_data_jws_header import (
    AttachDecoratorDataJWSHeader,
)


class AttachDecoratorData1JWS(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AttachDecoratorData1JWS - a model defined in OpenAPI
        header: The header of this AttachDecoratorData1JWS.
        signature: signature.
        protected: protected JWS header [Optional].
    """

    header: AttachDecoratorDataJWSHeader
    signature: str
    protected: Optional[str] = None

    @field_validator("protected")
    @classmethod
    def protected_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[-_a-zA-Z0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of protected does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("signature")
    @classmethod
    def signature_pattern(cls, value):
        pattern = r"^[-_a-zA-Z0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of signature does not match regex pattern ('{pattern}')"
            )
        return value
    model_config = ConfigDict(populate_by_name=True)


AttachDecoratorData1JWS.update_forward_refs()
