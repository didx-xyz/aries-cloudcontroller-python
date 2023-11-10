# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictStr, field_validator

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ConnectionStaticRequest(BaseModel):
    """
    ConnectionStaticRequest
    """

    alias: Optional[StrictStr] = Field(
        default=None, description="Alias to assign to this connection"
    )
    my_did: Optional[StrictStr] = Field(default=None, description="Local DID")
    my_seed: Optional[StrictStr] = Field(
        default=None, description="Seed to use for the local DID"
    )
    their_did: Optional[StrictStr] = Field(default=None, description="Remote DID")
    their_endpoint: Optional[StrictStr] = Field(
        default=None, description="URL endpoint for other party"
    )
    their_label: Optional[StrictStr] = Field(
        default=None, description="Other party's label for this connection"
    )
    their_seed: Optional[StrictStr] = Field(
        default=None, description="Seed to use for the remote DID"
    )
    their_verkey: Optional[StrictStr] = Field(
        default=None, description="Remote verification key"
    )
    __properties: ClassVar[List[str]] = [
        "alias",
        "my_did",
        "my_seed",
        "their_did",
        "their_endpoint",
        "their_label",
        "their_seed",
        "their_verkey",
    ]

    @field_validator("my_did")
    def my_did_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/"
            )
        return value

    @field_validator("their_did")
    def their_did_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/"
            )
        return value

    @field_validator("their_endpoint")
    def their_endpoint_validate_regular_expression(cls, value):
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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConnectionStaticRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of ConnectionStaticRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "alias": obj.get("alias"),
                "my_did": obj.get("my_did"),
                "my_seed": obj.get("my_seed"),
                "their_did": obj.get("their_did"),
                "their_endpoint": obj.get("their_endpoint"),
                "their_label": obj.get("their_label"),
                "their_seed": obj.get("their_seed"),
                "their_verkey": obj.get("their_verkey"),
            }
        )
        return _obj
