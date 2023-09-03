# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field, Extra  # noqa: F401


class MediationRecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MediationRecord - a model defined in OpenAPI
        connection_id: The connection_id of this MediationRecord.
        role: The role of this MediationRecord.
        created_at: Time of record creation [Optional].
        endpoint: The endpoint of this MediationRecord [Optional].
        mediation_id: The mediation_id of this MediationRecord [Optional].
        mediator_terms: The mediator_terms of this MediationRecord [Optional].
        recipient_terms: The recipient_terms of this MediationRecord [Optional].
        routing_keys: The routing_keys of this MediationRecord [Optional].
        state: Current record state [Optional].
        updated_at: Time of last record update [Optional].
    """

    connection_id: str
    role: str
    created_at: Optional[str] = None
    endpoint: Optional[str] = None
    mediation_id: Optional[str] = None
    mediator_terms: Optional[List[str]] = None
    recipient_terms: Optional[List[str]] = None
    routing_keys: Optional[List[str]] = None
    state: Optional[str] = None
    updated_at: Optional[str] = None

    @field_validator("created_at")
    @classmethod
    def created_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of created_at does not match regex pattern ('{pattern}')"
            )
        return value

    @field_validator("updated_at")
    @classmethod
    def updated_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of updated_at does not match regex pattern ('{pattern}')"
            )
        return value
    model_config = ConfigDict(populate_by_name=True)


MediationRecord.update_forward_refs()
