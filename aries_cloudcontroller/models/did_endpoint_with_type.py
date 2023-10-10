# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DIDEndpointWithType(BaseModel):
    """
    DIDEndpointWithType
    """
    did: Annotated[str, Field(strict=True)] = Field(description="DID of interest")
    endpoint: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Endpoint to set (omit to delete)")
    endpoint_type: Optional[StrictStr] = Field(default=None, description="Endpoint type to set (default 'Endpoint'); affects only public or posted DIDs")
    __properties: ClassVar[List[str]] = ["did", "endpoint", "endpoint_type"]

    @field_validator('did')
    def did_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$", value):
            raise ValueError(r"must validate the regular expression /^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/")
        return value

    @field_validator('endpoint')
    def endpoint_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$/")
        return value

    @field_validator('endpoint_type')
    def endpoint_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Endpoint', 'Profile', 'LinkedDomains'):
            raise ValueError("must be one of enum values ('Endpoint', 'Profile', 'LinkedDomains')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DIDEndpointWithType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of DIDEndpointWithType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "did": obj.get("did"),
            "endpoint": obj.get("endpoint"),
            "endpoint_type": obj.get("endpoint_type")
        })
        return _obj


