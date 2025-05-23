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
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

import orjson
from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.attach_decorator_data_jws import (
    AttachDecoratorDataJWS,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class AttachDecoratorData(BaseModel):
    """
    AttachDecoratorData
    """  # noqa: E501

    # keep custom changes
    var_base64: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Base64-encoded data", alias="base64"
    )
    var_json: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = Field(
        default=None, description="JSON-serialized data", alias="json"
    )
    jws: Optional[AttachDecoratorDataJWS] = Field(
        default=None, description="Detached Java Web Signature"
    )
    links: Optional[List[StrictStr]] = Field(
        default=None, description="List of hypertext links to data"
    )
    sha256: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="SHA256 hash (binhex encoded) of content"
    )
    __properties: ClassVar[List[str]] = ["base64", "json", "jws", "links", "sha256"]

    @field_validator("var_base64")
    def var_base64_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9+\/]*={0,2}$", value):
            raise ValueError(
                r"must validate the regular expression /^[a-zA-Z0-9+\/]*={0,2}$/"
            )
        return value

    @field_validator("sha256")
    def sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-fA-F0-9+\/]{64}$", value):
            raise ValueError(
                r"must validate the regular expression /^[a-fA-F0-9+\/]{64}$/"
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
        """Create an instance of AttachDecoratorData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of jws
        if self.jws:
            _dict["jws"] = self.jws.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AttachDecoratorData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "base64": obj.get("base64"),
                "json": obj.get("json"),
                "jws": (
                    AttachDecoratorDataJWS.from_dict(obj["jws"])
                    if obj.get("jws") is not None
                    else None
                ),
                "links": obj.get("links"),
                "sha256": obj.get("sha256"),
            }
        )
        return _obj
