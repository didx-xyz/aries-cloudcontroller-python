# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.3.0.post20250507
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.indy_rev_reg_def_value_public_keys import (
    IndyRevRegDefValuePublicKeys,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class IndyRevRegDefValue(BaseModel):
    """
    IndyRevRegDefValue
    """  # noqa: E501

    issuance_type: Optional[StrictStr] = Field(
        default=None, description="Issuance type", alias="issuanceType"
    )
    max_cred_num: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(
        default=None,
        description="Maximum number of credentials; registry size",
        alias="maxCredNum",
    )
    public_keys: Optional[IndyRevRegDefValuePublicKeys] = Field(
        default=None, description="Public keys", alias="publicKeys"
    )
    tails_hash: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Tails hash value", alias="tailsHash"
    )
    tails_location: Optional[StrictStr] = Field(
        default=None, description="Tails file location", alias="tailsLocation"
    )
    __properties: ClassVar[List[str]] = [
        "issuanceType",
        "maxCredNum",
        "publicKeys",
        "tailsHash",
        "tailsLocation",
    ]

    @field_validator("issuance_type")
    def issuance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["ISSUANCE_ON_DEMAND", "ISSUANCE_BY_DEFAULT"]):
            raise ValueError(
                "must be one of enum values ('ISSUANCE_ON_DEMAND', 'ISSUANCE_BY_DEFAULT')"
            )
        return value

    @field_validator("tails_hash")
    def tails_hash_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$/"
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
        """Create an instance of IndyRevRegDefValue from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of public_keys
        if self.public_keys:
            _dict["publicKeys"] = self.public_keys.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndyRevRegDefValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "issuanceType": obj.get("issuanceType"),
                "maxCredNum": obj.get("maxCredNum"),
                "publicKeys": (
                    IndyRevRegDefValuePublicKeys.from_dict(obj["publicKeys"])
                    if obj.get("publicKeys") is not None
                    else None
                ),
                "tailsHash": obj.get("tailsHash"),
                "tailsLocation": obj.get("tailsLocation"),
            }
        )
        return _obj
