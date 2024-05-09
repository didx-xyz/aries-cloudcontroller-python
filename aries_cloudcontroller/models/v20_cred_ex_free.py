# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.12.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.v20_cred_filter import V20CredFilter
from aries_cloudcontroller.models.v20_cred_preview import V20CredPreview
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class V20CredExFree(BaseModel):
    """
    V20CredExFree
    """  # noqa: E501

    auto_remove: Optional[StrictBool] = Field(
        default=None,
        description="Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting)",
    )
    comment: Optional[StrictStr] = Field(
        default=None, description="Human-readable comment"
    )
    connection_id: StrictStr = Field(description="Connection identifier")
    credential_preview: Optional[V20CredPreview] = None
    filter: V20CredFilter = Field(
        description="Credential specification criteria by format"
    )
    replacement_id: Optional[StrictStr] = Field(
        default=None,
        description="Optional identifier used to manage credential replacement",
    )
    trace: Optional[StrictBool] = Field(
        default=None,
        description="Record trace information, based on agent configuration",
    )
    verification_method: Optional[StrictStr] = Field(
        default=None, description="For ld-proofs. Verification method for signing."
    )
    __properties: ClassVar[List[str]] = [
        "auto_remove",
        "comment",
        "connection_id",
        "credential_preview",
        "filter",
        "replacement_id",
        "trace",
        "verification_method",
    ]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V20CredExFree from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credential_preview
        if self.credential_preview:
            _dict["credential_preview"] = self.credential_preview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict["filter"] = self.filter.to_dict()
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict["comment"] = None

        # set to None if replacement_id (nullable) is None
        # and model_fields_set contains the field
        if self.replacement_id is None and "replacement_id" in self.model_fields_set:
            _dict["replacement_id"] = None

        # set to None if verification_method (nullable) is None
        # and model_fields_set contains the field
        if (
            self.verification_method is None
            and "verification_method" in self.model_fields_set
        ):
            _dict["verification_method"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V20CredExFree from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "auto_remove": obj.get("auto_remove"),
                "comment": obj.get("comment"),
                "connection_id": obj.get("connection_id"),
                "credential_preview": (
                    V20CredPreview.from_dict(obj["credential_preview"])
                    if obj.get("credential_preview") is not None
                    else None
                ),
                "filter": (
                    V20CredFilter.from_dict(obj["filter"])
                    if obj.get("filter") is not None
                    else None
                ),
                "replacement_id": obj.get("replacement_id"),
                "trace": obj.get("trace"),
                "verification_method": obj.get("verification_method"),
            }
        )
        return _obj
