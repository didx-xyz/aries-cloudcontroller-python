# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field, Extra  # noqa: F401


class CredentialDefinitionSendRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredentialDefinitionSendRequest - a model defined in OpenAPI
        revocation_registry_size: Revocation registry size [Optional].
        schema_id: Schema identifier [Optional].
        support_revocation: Revocation supported flag [Optional].
        tag: Credential definition identifier tag [Optional].
    """

    revocation_registry_size: Optional[int] = None
    schema_id: Optional[str] = None
    support_revocation: Optional[bool] = None
    tag: Optional[str] = None

    @field_validator("revocation_registry_size")
    @classmethod
    def revocation_registry_size_max(cls, value):
        # Property is optional
        if value is None:
            return

        if value > 32768:
            raise ValueError(
                f"revocation_registry_size must be less than 32768, currently {value}"
            )
        return value

    @field_validator("revocation_registry_size")
    @classmethod
    def revocation_registry_size_min(cls, value):
        # Property is optional
        if value is None:
            return

        if value < 4:
            raise ValueError(
                f"revocation_registry_size must be greater than 4, currently {value}"
            )
        return value

    @field_validator("schema_id")
    @classmethod
    def schema_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_id does not match regex pattern ('{pattern}')"
            )
        return value
    model_config = ConfigDict(populate_by_name=True)


CredentialDefinitionSendRequest.update_forward_refs()
