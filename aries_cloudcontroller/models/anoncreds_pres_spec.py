# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.2.1.post20250327
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.anoncreds_requested_creds_requested_attr import (
    AnoncredsRequestedCredsRequestedAttr,
)
from aries_cloudcontroller.models.anoncreds_requested_creds_requested_pred import (
    AnoncredsRequestedCredsRequestedPred,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class AnoncredsPresSpec(BaseModel):
    """
    AnoncredsPresSpec
    """  # noqa: E501

    requested_attributes: Dict[str, AnoncredsRequestedCredsRequestedAttr] = Field(
        description="Nested object mapping proof request attribute referents to requested-attribute specifiers"
    )
    requested_predicates: Dict[str, AnoncredsRequestedCredsRequestedPred] = Field(
        description="Nested object mapping proof request predicate referents to requested-predicate specifiers"
    )
    self_attested_attributes: Dict[str, StrictStr] = Field(
        description="Self-attested attributes to build into proof"
    )
    trace: Optional[StrictBool] = Field(
        default=None, description="Whether to trace event (default false)"
    )
    __properties: ClassVar[List[str]] = [
        "requested_attributes",
        "requested_predicates",
        "self_attested_attributes",
        "trace",
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
        """Create an instance of AnoncredsPresSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in requested_attributes (dict)
        _field_dict = {}
        if self.requested_attributes:
            for _key_requested_attributes in self.requested_attributes:
                if self.requested_attributes[_key_requested_attributes]:
                    _field_dict[_key_requested_attributes] = self.requested_attributes[
                        _key_requested_attributes
                    ].to_dict()
            _dict["requested_attributes"] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in requested_predicates (dict)
        _field_dict = {}
        if self.requested_predicates:
            for _key_requested_predicates in self.requested_predicates:
                if self.requested_predicates[_key_requested_predicates]:
                    _field_dict[_key_requested_predicates] = self.requested_predicates[
                        _key_requested_predicates
                    ].to_dict()
            _dict["requested_predicates"] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnoncredsPresSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "requested_attributes": (
                    dict(
                        (_k, AnoncredsRequestedCredsRequestedAttr.from_dict(_v))
                        for _k, _v in obj["requested_attributes"].items()
                    )
                    if obj.get("requested_attributes") is not None
                    else None
                ),
                "requested_predicates": (
                    dict(
                        (_k, AnoncredsRequestedCredsRequestedPred.from_dict(_v))
                        for _k, _v in obj["requested_predicates"].items()
                    )
                    if obj.get("requested_predicates") is not None
                    else None
                ),
                "self_attested_attributes": obj.get("self_attested_attributes"),
                "trace": obj.get("trace"),
            }
        )
        return _obj
