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


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from aries_cloudcontroller.models.attach_decorator_data_jws import AttachDecoratorDataJWS
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AttachDecoratorData(BaseModel):
    """
    AttachDecoratorData
    """
    var_base64: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Base64-encoded data", alias="base64")
    var_json: Optional[Union[str, Any]] = Field(default=None, description="JSON-serialized data", alias="json")
    jws: Optional[AttachDecoratorDataJWS] = None
    links: Optional[List[StrictStr]] = Field(default=None, description="List of hypertext links to data")
    sha256: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="SHA256 hash (binhex encoded) of content")
    __properties: ClassVar[List[str]] = ["base64", "json", "jws", "links", "sha256"]

    @field_validator('var_base64')
    def var_base64_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9+\/]*={0,2}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9+\/]*={0,2}$/")
        return value

    @field_validator('sha256')
    def sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-fA-F0-9+\/]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9+\/]{64}$/")
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
        return json.model_dump_json(self.to_dict(), by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AttachDecoratorData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of jws
        if self.jws:
            _dict['jws'] = self.jws.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of AttachDecoratorData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "base64": obj.get("base64"),
            "json": obj.get("json"),
            "jws": AttachDecoratorDataJWS.from_dict(obj.get("jws")) if obj.get("jws") is not None else None,
            "links": obj.get("links"),
            "sha256": obj.get("sha256")
        })
        return _obj


