# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.10.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Union

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Filter(BaseModel):
    """
    Filter
    """  # noqa: E501

    const: Optional[Union[str, int, float]] = Field(default=None, description="Const")
    enum: Optional[List[Union[str, int, float]]] = None
    exclusive_maximum: Optional[Union[str, int, float]] = Field(
        default=None, description="ExclusiveMaximum", alias="exclusiveMaximum"
    )
    exclusive_minimum: Optional[Union[str, int, float]] = Field(
        default=None, description="ExclusiveMinimum", alias="exclusiveMinimum"
    )
    format: Optional[StrictStr] = Field(default=None, description="Format")
    max_length: Optional[StrictInt] = Field(
        default=None, description="Max Length", alias="maxLength"
    )
    maximum: Optional[Union[str, int, float]] = Field(
        default=None, description="Maximum"
    )
    min_length: Optional[StrictInt] = Field(
        default=None, description="Min Length", alias="minLength"
    )
    minimum: Optional[Union[str, int, float]] = Field(
        default=None, description="Minimum"
    )
    var_not: Optional[StrictBool] = Field(default=None, description="Not", alias="not")
    pattern: Optional[StrictStr] = Field(default=None, description="Pattern")
    type: Optional[StrictStr] = Field(default=None, description="Type")
    __properties: ClassVar[List[str]] = [
        "const",
        "enum",
        "exclusiveMaximum",
        "exclusiveMinimum",
        "format",
        "maxLength",
        "maximum",
        "minLength",
        "minimum",
        "not",
        "pattern",
        "type",
    ]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Filter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Filter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "const": obj.get("const"),
                "enum": obj.get("enum"),
                "exclusiveMaximum": obj.get("exclusiveMaximum"),
                "exclusiveMinimum": obj.get("exclusiveMinimum"),
                "format": obj.get("format"),
                "maxLength": obj.get("maxLength"),
                "maximum": obj.get("maximum"),
                "minLength": obj.get("minLength"),
                "minimum": obj.get("minimum"),
                "not": obj.get("not"),
                "pattern": obj.get("pattern"),
                "type": obj.get("type"),
            }
        )
        return _obj
