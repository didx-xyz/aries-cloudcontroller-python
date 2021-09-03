# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.constraints import Constraints
from aries_cloudcontroller.model.schema_input_descriptor import SchemaInputDescriptor


class InputDescriptors(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    InputDescriptors - a model defined in OpenAPI
        constraints: The constraints of this InputDescriptors [Optional].
        group: The group of this InputDescriptors [Optional].
        id: ID [Optional].
        metadata: Metadata dictionary [Optional].
        name: Name [Optional].
        purpose: Purpose [Optional].
        schema_: The schema_ of this InputDescriptors [Optional].
    """

    constraints: Optional[Constraints] = None
    group: Optional[List[str]] = None
    id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    purpose: Optional[str] = None
    schema_: Optional[List[SchemaInputDescriptor]] = Field(None, alias="schema")

    def __init__(
        self,
        *,
        constraints: Optional[Constraints] = None,
        group: Optional[List[str]] = None,
        id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        purpose: Optional[str] = None,
        schema_: Optional[List[SchemaInputDescriptor]] = None,
        **kwargs,
    ):
        super().__init__(
            constraints=constraints,
            group=group,
            id=id,
            metadata=metadata,
            name=name,
            purpose=purpose,
            schema_=schema_,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


InputDescriptors.update_forward_refs()