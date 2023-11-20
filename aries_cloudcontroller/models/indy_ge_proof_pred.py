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
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class IndyGEProofPred(BaseModel):
    """
    IndyGEProofPred
    """  # noqa: E501

    attr_name: Optional[StrictStr] = Field(
        default=None, description="Attribute name, indy-canonicalized"
    )
    p_type: Optional[StrictStr] = Field(default=None, description="Predicate type")
    value: Optional[StrictInt] = Field(
        default=None, description="Predicate threshold value"
    )
    __properties: ClassVar[List[str]] = ["attr_name", "p_type", "value"]

    @field_validator("p_type")
    def p_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("LT", "LE", "GE", "GT"):
            raise ValueError("must be one of enum values ('LT', 'LE', 'GE', 'GT')")
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
        """Create an instance of IndyGEProofPred from a JSON string"""
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
        """Create an instance of IndyGEProofPred from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "attr_name": obj.get("attr_name"),
                "p_type": obj.get("p_type"),
                "value": obj.get("value"),
            }
        )
        return _obj
