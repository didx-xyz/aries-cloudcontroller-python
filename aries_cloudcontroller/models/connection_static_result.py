# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.3.0rc1.post20250417
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

from aries_cloudcontroller.models.conn_record import ConnRecord
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class ConnectionStaticResult(BaseModel):
    """
    ConnectionStaticResult
    """  # noqa: E501

    my_did: Annotated[str, Field(strict=True)] = Field(description="Local DID")
    my_endpoint: Annotated[str, Field(strict=True)] = Field(
        description="My URL endpoint"
    )
    my_verkey: Annotated[str, Field(strict=True)] = Field(
        description="My verification key"
    )
    record: ConnRecord
    their_did: Annotated[str, Field(strict=True)] = Field(description="Remote DID")
    their_verkey: Annotated[str, Field(strict=True)] = Field(
        description="Remote verification key"
    )
    __properties: ClassVar[List[str]] = [
        "my_did",
        "my_endpoint",
        "my_verkey",
        "record",
        "their_did",
        "their_verkey",
    ]

    @field_validator("my_did")
    def my_did_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/"
            )
        return value

    @field_validator("my_endpoint")
    def my_endpoint_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(
            r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$/"
            )
        return value

    @field_validator("my_verkey")
    def my_verkey_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$/"
            )
        return value

    @field_validator("their_did")
    def their_did_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/"
            )
        return value

    @field_validator("their_verkey")
    def their_verkey_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
        """Create an instance of ConnectionStaticResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of record
        if self.record:
            _dict["record"] = self.record.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectionStaticResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "my_did": obj.get("my_did"),
                "my_endpoint": obj.get("my_endpoint"),
                "my_verkey": obj.get("my_verkey"),
                "record": (
                    ConnRecord.from_dict(obj["record"])
                    if obj.get("record") is not None
                    else None
                ),
                "their_did": obj.get("their_did"),
                "their_verkey": obj.get("their_verkey"),
            }
        )
        return _obj
