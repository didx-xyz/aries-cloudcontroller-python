# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.0.0rc5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.presentation_definition import PresentationDefinition
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class DIFPresSpec(BaseModel):
    """
    DIFPresSpec
    """  # noqa: E501

    issuer_id: Optional[StrictStr] = Field(
        default=None,
        description="Issuer identifier to sign the presentation, if different from current public DID",
    )
    presentation_definition: Optional[PresentationDefinition] = None
    record_ids: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Mapping of input_descriptor id to list of stored W3C credential record_id",
    )
    reveal_doc: Optional[Dict[str, Any]] = Field(
        default=None,
        description="reveal doc [JSON-LD frame] dict used to derive the credential when selective disclosure is required",
    )
    __properties: ClassVar[List[str]] = [
        "issuer_id",
        "presentation_definition",
        "record_ids",
        "reveal_doc",
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
        """Create an instance of DIFPresSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of presentation_definition
        if self.presentation_definition:
            _dict["presentation_definition"] = self.presentation_definition.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DIFPresSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "issuer_id": obj.get("issuer_id"),
                "presentation_definition": (
                    PresentationDefinition.from_dict(obj["presentation_definition"])
                    if obj.get("presentation_definition") is not None
                    else None
                ),
                "record_ids": obj.get("record_ids"),
                "reveal_doc": obj.get("reveal_doc"),
            }
        )
        return _obj
