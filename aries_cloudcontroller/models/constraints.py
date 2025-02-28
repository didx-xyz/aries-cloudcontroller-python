# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.2.1.post20250228
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Self

from aries_cloudcontroller.models.dif_field import DIFField
from aries_cloudcontroller.models.dif_holder import DIFHolder
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class Constraints(BaseModel):
    """
    Constraints
    """  # noqa: E501

    fields: Optional[List[DIFField]] = None
    is_holder: Optional[List[DIFHolder]] = None
    limit_disclosure: Optional[StrictStr] = Field(
        default=None, description="LimitDisclosure"
    )
    status_active: Optional[StrictStr] = None
    status_revoked: Optional[StrictStr] = None
    status_suspended: Optional[StrictStr] = None
    subject_is_issuer: Optional[StrictStr] = Field(
        default=None, description="SubjectIsIssuer"
    )
    __properties: ClassVar[List[str]] = [
        "fields",
        "is_holder",
        "limit_disclosure",
        "status_active",
        "status_revoked",
        "status_suspended",
        "subject_is_issuer",
    ]

    @field_validator("status_active")
    def status_active_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["required", "allowed", "disallowed"]):
            raise ValueError(
                "must be one of enum values ('required', 'allowed', 'disallowed')"
            )
        return value

    @field_validator("status_revoked")
    def status_revoked_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["required", "allowed", "disallowed"]):
            raise ValueError(
                "must be one of enum values ('required', 'allowed', 'disallowed')"
            )
        return value

    @field_validator("status_suspended")
    def status_suspended_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["required", "allowed", "disallowed"]):
            raise ValueError(
                "must be one of enum values ('required', 'allowed', 'disallowed')"
            )
        return value

    @field_validator("subject_is_issuer")
    def subject_is_issuer_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["required", "preferred"]):
            raise ValueError("must be one of enum values ('required', 'preferred')")
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
        """Create an instance of Constraints from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item_fields in self.fields:
                if _item_fields:
                    _items.append(_item_fields.to_dict())
            _dict["fields"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in is_holder (list)
        _items = []
        if self.is_holder:
            for _item_is_holder in self.is_holder:
                if _item_is_holder:
                    _items.append(_item_is_holder.to_dict())
            _dict["is_holder"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Constraints from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "fields": (
                    [DIFField.from_dict(_item) for _item in obj["fields"]]
                    if obj.get("fields") is not None
                    else None
                ),
                "is_holder": (
                    [DIFHolder.from_dict(_item) for _item in obj["is_holder"]]
                    if obj.get("is_holder") is not None
                    else None
                ),
                "limit_disclosure": obj.get("limit_disclosure"),
                "status_active": obj.get("status_active"),
                "status_revoked": obj.get("status_revoked"),
                "status_suspended": obj.get("status_suspended"),
                "subject_is_issuer": obj.get("subject_is_issuer"),
            }
        )
        return _obj
