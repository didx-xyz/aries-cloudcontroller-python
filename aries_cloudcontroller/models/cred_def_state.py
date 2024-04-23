# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.12.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Self

from aries_cloudcontroller.models.cred_def import CredDef
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class CredDefState(BaseModel):
    """
    CredDefState
    """  # noqa: E501

    credential_definition: Optional[CredDef] = Field(
        default=None, description="credential definition"
    )
    credential_definition_id: Optional[StrictStr] = Field(
        default=None, description="credential definition id"
    )
    state: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "credential_definition",
        "credential_definition_id",
        "state",
    ]

    @field_validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["finished", "failed", "action", "wait"]):
            raise ValueError(
                "must be one of enum values ('finished', 'failed', 'action', 'wait')"
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
        """Create an instance of CredDefState from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credential_definition
        if self.credential_definition:
            _dict["credential_definition"] = self.credential_definition.to_dict()
        # set to None if credential_definition_id (nullable) is None
        # and model_fields_set contains the field
        if (
            self.credential_definition_id is None
            and "credential_definition_id" in self.model_fields_set
        ):
            _dict["credential_definition_id"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CredDefState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "credential_definition": (
                    CredDef.from_dict(obj["credential_definition"])
                    if obj.get("credential_definition") is not None
                    else None
                ),
                "credential_definition_id": obj.get("credential_definition_id"),
                "state": obj.get("state"),
            }
        )
        return _obj