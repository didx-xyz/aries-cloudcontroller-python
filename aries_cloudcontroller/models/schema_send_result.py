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
from pydantic import BaseModel, field_validator
from pydantic import Field
from typing_extensions import Annotated
from aries_cloudcontroller.models.model_schema import ModelSchema
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SchemaSendResult(BaseModel):
    """
    SchemaSendResult
    """
    var_schema: Optional[ModelSchema] = Field(default=None, alias="schema")
    schema_id: Annotated[str, Field(strict=True)] = Field(description="Schema identifier")
    __properties: ClassVar[List[str]] = ["schema", "schema_id"]

    @field_validator('schema_id')
    def schema_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$", value):
            raise ValueError(r"must validate the regular expression /^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$/")
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
        """Create an instance of SchemaSendResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of SchemaSendResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": ModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "schema_id": obj.get("schema_id")
        })
        return _obj


