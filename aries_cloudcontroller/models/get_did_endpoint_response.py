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
from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class GetDIDEndpointResponse(BaseModel):
    """
    GetDIDEndpointResponse
    """  # noqa: E501

    endpoint: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Full verification key"
    )
    __properties: ClassVar[List[str]] = ["endpoint"]

    @field_validator("endpoint")
    def endpoint_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$/"
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
        """Create an instance of GetDIDEndpointResponse from a JSON string"""
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
        # set to None if endpoint (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint is None and "endpoint" in self.model_fields_set:
            _dict["endpoint"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetDIDEndpointResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({"endpoint": obj.get("endpoint")})
        return _obj
