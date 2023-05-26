# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class IndyPresPredSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyPresPredSpec - a model defined in OpenAPI
        name: Attribute name.
        predicate: Predicate type ('<', '<=', '>=', or '>').
        threshold: Threshold value.
        cred_def_id: Credential definition identifier [Optional].
    """

    name: str
    predicate: Literal["<", "<=", ">=", ">"]
    threshold: int
    cred_def_id: Optional[str] = None

    @validator("cred_def_id")
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

    class Config:
        allow_population_by_field_name = True


IndyPresPredSpec.update_forward_refs()
