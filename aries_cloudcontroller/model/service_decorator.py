# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import (
    ConfigDict,
    AnyUrl,
    BaseModel,
    EmailStr,
    validator,
    Field,
    Extra,
)  # noqa: F401


class ServiceDecorator(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceDecorator - a model defined in OpenAPI
        recipient_keys: List of recipient keys [Optional].
        service_endpoint: Service endpoint at which to reach this agent [Optional].
        routing_keys: List of routing keys [Optional].
    """

    recipient_keys: Optional[List[str]] = Field(None, alias="recipientKeys")
    service_endpoint: Optional[str] = Field(None, alias="serviceEndpoint")
    routing_keys: Optional[List[str]] = Field(None, alias="routingKeys")
    model_config = ConfigDict(populate_by_name=True)


ServiceDecorator.model_rebuild()
