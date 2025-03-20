# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.2.1.post20250319
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Self

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class CreateWalletRequest(BaseModel):
    """
    CreateWalletRequest
    """  # noqa: E501

    extra_settings: Optional[Dict[str, Any]] = Field(
        default=None, description="Agent config key-value pairs"
    )
    image_url: Optional[StrictStr] = Field(
        default=None,
        description="Image url for this wallet. This image url is publicized (self-attested) to other agents as part of forming a connection.",
    )
    key_management_mode: Optional[StrictStr] = Field(
        default=None, description="Key management method to use for this wallet."
    )
    label: Optional[StrictStr] = Field(
        default=None,
        description="Label for this wallet. This label is publicized (self-attested) to other agents as part of forming a connection.",
    )
    wallet_dispatch_type: Optional[StrictStr] = Field(
        default=None,
        description="Webhook target dispatch type for this wallet. default: Dispatch only to webhooks associated with this wallet. base: Dispatch only to webhooks associated with the base wallet. both: Dispatch to both webhook targets.",
    )
    wallet_key: Optional[StrictStr] = Field(
        default=None, description="Master key used for key derivation."
    )
    wallet_key_derivation: Optional[StrictStr] = Field(
        default=None, description="Key derivation"
    )
    wallet_name: Optional[StrictStr] = Field(default=None, description="Wallet name")
    wallet_type: Optional[StrictStr] = Field(
        default=None,
        description="Type of the wallet to create. Must be same as base wallet.",
    )
    wallet_webhook_urls: Optional[List[StrictStr]] = Field(
        default=None, description="List of Webhook URLs associated with this subwallet"
    )
    __properties: ClassVar[List[str]] = [
        "extra_settings",
        "image_url",
        "key_management_mode",
        "label",
        "wallet_dispatch_type",
        "wallet_key",
        "wallet_key_derivation",
        "wallet_name",
        "wallet_type",
        "wallet_webhook_urls",
    ]

    @field_validator("key_management_mode")
    def key_management_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["managed"]):
            raise ValueError("must be one of enum values ('managed')")
        return value

    @field_validator("wallet_dispatch_type")
    def wallet_dispatch_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["default", "both", "base"]):
            raise ValueError("must be one of enum values ('default', 'both', 'base')")
        return value

    @field_validator("wallet_key_derivation")
    def wallet_key_derivation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["ARGON2I_MOD", "ARGON2I_INT", "RAW"]):
            raise ValueError(
                "must be one of enum values ('ARGON2I_MOD', 'ARGON2I_INT', 'RAW')"
            )
        return value

    @field_validator("wallet_type")
    def wallet_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["askar", "askar-anoncreds"]):
            raise ValueError("must be one of enum values ('askar', 'askar-anoncreds')")
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
        """Create an instance of CreateWalletRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateWalletRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "extra_settings": obj.get("extra_settings"),
                "image_url": obj.get("image_url"),
                "key_management_mode": obj.get("key_management_mode"),
                "label": obj.get("label"),
                "wallet_dispatch_type": obj.get("wallet_dispatch_type"),
                "wallet_key": obj.get("wallet_key"),
                "wallet_key_derivation": obj.get("wallet_key_derivation"),
                "wallet_name": obj.get("wallet_name"),
                "wallet_type": obj.get("wallet_type"),
                "wallet_webhook_urls": obj.get("wallet_webhook_urls"),
            }
        )
        return _obj
