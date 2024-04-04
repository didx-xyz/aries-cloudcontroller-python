# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.indy_ge_proof_pred import IndyGEProofPred
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class IndyGEProof(BaseModel):
    """
    IndyGEProof
    """  # noqa: E501

    alpha: Optional[Annotated[str, Field(strict=True)]] = None
    mj: Optional[Annotated[str, Field(strict=True)]] = None
    predicate: Optional[IndyGEProofPred] = None
    r: Optional[Dict[str, Annotated[str, Field(strict=True)]]] = None
    t: Optional[Dict[str, Annotated[str, Field(strict=True)]]] = None
    u: Optional[Dict[str, Annotated[str, Field(strict=True)]]] = None
    __properties: ClassVar[List[str]] = ["alpha", "mj", "predicate", "r", "t", "u"]

    @field_validator("alpha")
    def alpha_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]*$/")
        return value

    @field_validator("mj")
    def mj_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]*$/")
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
        """Create an instance of IndyGEProof from a JSON string"""
        return cls.from_dict(json.loads(json_str))

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
        # override the default output from pydantic by calling `to_dict()` of predicate
        if self.predicate:
            _dict["predicate"] = self.predicate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndyGEProof from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "alpha": obj.get("alpha"),
                "mj": obj.get("mj"),
                "predicate": (
                    IndyGEProofPred.from_dict(obj.get("predicate"))
                    if obj.get("predicate") is not None
                    else None
                ),
                "r": obj.get("r"),
                "t": obj.get("t"),
                "u": obj.get("u"),
            }
        )
        return _obj
