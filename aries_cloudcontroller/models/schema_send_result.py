# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.2.1.post20250228
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.model_schema import ModelSchema
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class SchemaSendResult(BaseModel):
    """
    SchemaSendResult
    """  # noqa: E501

    var_schema: Optional[ModelSchema] = Field(
        default=None, description="Schema definition", alias="schema"
    )
    schema_id: Annotated[str, Field(strict=True)] = Field(
        description="Schema identifier"
    )
    __properties: ClassVar[List[str]] = ["schema", "schema_id"]

    @field_validator("schema_id")
    def schema_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$/"
            )
        return value

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SchemaSendResult from a JSON string"""
        return cls.from_dict(orjson.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict["schema"] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SchemaSendResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "schema": (
                    ModelSchema.from_dict(obj["schema"])
                    if obj.get("schema") is not None
                    else None
                ),
                "schema_id": obj.get("schema_id"),
            }
        )
        return _obj
