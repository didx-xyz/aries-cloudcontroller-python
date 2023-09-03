# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field, Extra  # noqa: F401


class AttachDecoratorDataJWSHeader(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AttachDecoratorDataJWSHeader - a model defined in OpenAPI
        kid: Key identifier, in W3C did:key or DID URL format.
    """

    kid: str

    @field_validator("kid")
    @classmethod
    def kid_pattern(cls, value):
        pattern = r"^did:(?:key:z[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]+|sov:[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}(;.*)?(\?.*)?#.+)$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of kid does not match regex pattern ('{pattern}')")
        return value
    model_config = ConfigDict(populate_by_name=True)


AttachDecoratorDataJWSHeader.update_forward_refs()
