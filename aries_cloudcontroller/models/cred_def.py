# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.0.0b0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Self

from aries_cloudcontroller.models.cred_def_value_schema_anoncreds import (
    CredDefValueSchemaAnoncreds,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class CredDef(BaseModel):
    """
    CredDef
    """  # noqa: E501

    issuer_id: Optional[StrictStr] = Field(
        default=None,
        description="Issuer Identifier of the credential definition or schema",
        alias="issuerId",
    )
    schema_id: Optional[StrictStr] = Field(
        default=None, description="Schema identifier", alias="schemaId"
    )
    tag: Optional[StrictStr] = Field(
        default=None,
        description="The tag value passed in by the Issuer to an AnonCred's Credential Definition create and store implementation.",
    )
    type: Optional[StrictStr] = None
    value: Optional[CredDefValueSchemaAnoncreds] = None
    __properties: ClassVar[List[str]] = ["issuerId", "schemaId", "tag", "type", "value"]

    @field_validator("type")
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["CL"]):
            raise ValueError("must be one of enum values ('CL')")
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
        """Create an instance of CredDef from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict["value"] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CredDef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "issuerId": obj.get("issuerId"),
                "schemaId": obj.get("schemaId"),
                "tag": obj.get("tag"),
                "type": obj.get("type"),
                "value": (
                    CredDefValueSchemaAnoncreds.from_dict(obj["value"])
                    if obj.get("value") is not None
                    else None
                ),
            }
        )
        return _obj
