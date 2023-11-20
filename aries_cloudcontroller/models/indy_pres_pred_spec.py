# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.10.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator
from typing_extensions import Annotated

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class IndyPresPredSpec(BaseModel):
    """
    IndyPresPredSpec
    """  # noqa: E501

    cred_def_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Credential definition identifier"
    )
    name: StrictStr = Field(description="Attribute name")
    predicate: StrictStr = Field(description="Predicate type ('<', '<=', '>=', or '>')")
    threshold: StrictInt = Field(description="Threshold value")
    __properties: ClassVar[List[str]] = [
        "cred_def_id",
        "name",
        "predicate",
        "threshold",
    ]

    @field_validator("cred_def_id")
    def cred_def_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$/"
            )
        return value

    @field_validator("predicate")
    def predicate_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ("<", "<=", ">=", ">"):
            raise ValueError("must be one of enum values ('<', '<=', '>=', '>')")
        return value

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IndyPresPredSpec from a JSON string"""
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
        """Create an instance of IndyPresPredSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cred_def_id": obj.get("cred_def_id"),
                "name": obj.get("name"),
                "predicate": obj.get("predicate"),
                "threshold": obj.get("threshold"),
            }
        )
        return _obj
