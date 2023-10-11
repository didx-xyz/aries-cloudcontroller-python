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

from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing_extensions import Annotated

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class RevokeRequest(BaseModel):
    """
    RevokeRequest
    """

    comment: Optional[StrictStr] = Field(
        default=None,
        description="Optional comment to include in revocation notification",
    )
    connection_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="Connection ID to which the revocation notification will be sent; required if notify is true",
    )
    cred_ex_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Credential exchange identifier"
    )
    cred_rev_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Credential revocation identifier"
    )
    notify: Optional[StrictBool] = Field(
        default=None, description="Send a notification to the credential recipient"
    )
    notify_version: Optional[StrictStr] = Field(
        default=None,
        description="Specify which version of the revocation notification should be sent",
    )
    publish: Optional[StrictBool] = Field(
        default=None,
        description="(True) publish revocation to ledger immediately, or (default, False) mark it pending",
    )
    rev_reg_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Revocation registry identifier"
    )
    thread_id: Optional[StrictStr] = Field(
        default=None,
        description="Thread ID of the credential exchange message thread resulting in the credential now being revoked; required if notify is true",
    )
    __properties: ClassVar[List[str]] = [
        "comment",
        "connection_id",
        "cred_ex_id",
        "cred_rev_id",
        "notify",
        "notify_version",
        "publish",
        "rev_reg_id",
        "thread_id",
    ]

    @field_validator("connection_id")
    def connection_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}/"
            )
        return value

    @field_validator("cred_ex_id")
    def cred_ex_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}/"
            )
        return value

    @field_validator("cred_rev_id")
    def cred_rev_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[1-9][0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[1-9][0-9]*$/")
        return value

    @field_validator("notify_version")
    def notify_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("v1_0", "v2_0"):
            raise ValueError("must be one of enum values ('v1_0', 'v2_0')")
        return value

    @field_validator("rev_reg_id")
    def rev_reg_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)/"
            )
        return value

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RevokeRequest from a JSON string"""
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
        """Create an instance of RevokeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "comment": obj.get("comment"),
                "connection_id": obj.get("connection_id"),
                "cred_ex_id": obj.get("cred_ex_id"),
                "cred_rev_id": obj.get("cred_rev_id"),
                "notify": obj.get("notify"),
                "notify_version": obj.get("notify_version"),
                "publish": obj.get("publish"),
                "rev_reg_id": obj.get("rev_reg_id"),
                "thread_id": obj.get("thread_id"),
            }
        )
        return _obj
