# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class RevRegCreateRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RevRegCreateRequest - a model defined in OpenAPI
        credential_definition_id: Credential definition identifier [Optional].
        max_cred_num: Revocation registry size [Optional].
    """

    credential_definition_id: Optional[str] = None
    max_cred_num: Optional[int] = None

    def __init__(
        self,
        *,
        credential_definition_id: Optional[str] = None,
        max_cred_num: Optional[int] = None,
        **kwargs,
    ):
        super().__init__(
            credential_definition_id=credential_definition_id,
            max_cred_num=max_cred_num,
            **kwargs,
        )

    @validator("credential_definition_id")
    def credential_definition_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of credential_definition_id does not match regex pattern ('{pattern}')")
        return value

    @validator("max_cred_num")
    def max_cred_num_max(cls, value):
        # Property is optional
        if value is None:
            return

        if value > 32768:
            raise ValueError(f"max_cred_num must be less than 32768, currently {value}")
        return value

    @validator("max_cred_num")
    def max_cred_num_min(cls, value):
        # Property is optional
        if value is None:
            return

        if value < 4:
            raise ValueError(f"max_cred_num must be greater than 4, currently {value}")
        return value


RevRegCreateRequest.update_forward_refs()
