# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.claim_format import ClaimFormat
from aries_cloudcontroller.models.input_descriptors import InputDescriptors
from aries_cloudcontroller.models.submission_requirements import SubmissionRequirements
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class PresentationDefinition(BaseModel):
    """
    PresentationDefinition
    """  # noqa: E501

    format: Optional[ClaimFormat] = None
    id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Unique Resource Identifier"
    )
    input_descriptors: Optional[List[InputDescriptors]] = None
    name: Optional[StrictStr] = Field(
        default=None,
        description="Human-friendly name that describes what the presentation definition pertains to",
    )
    purpose: Optional[StrictStr] = Field(
        default=None,
        description="Describes the purpose for which the Presentation Definition's inputs are being requested",
    )
    submission_requirements: Optional[List[SubmissionRequirements]] = None
    __properties: ClassVar[List[str]] = [
        "format",
        "id",
        "input_descriptors",
        "name",
        "purpose",
        "submission_requirements",
    ]

    @field_validator("id")
    def id_validate_regular_expression(cls, value):
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

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PresentationDefinition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of format
        if self.format:
            _dict["format"] = self.format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in input_descriptors (list)
        _items = []
        if self.input_descriptors:
            for _item in self.input_descriptors:
                if _item:
                    _items.append(_item.to_dict())
            _dict["input_descriptors"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in submission_requirements (list)
        _items = []
        if self.submission_requirements:
            for _item in self.submission_requirements:
                if _item:
                    _items.append(_item.to_dict())
            _dict["submission_requirements"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PresentationDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "format": (
                    ClaimFormat.from_dict(obj.get("format"))
                    if obj.get("format") is not None
                    else None
                ),
                "id": obj.get("id"),
                "input_descriptors": (
                    [
                        InputDescriptors.from_dict(_item)
                        for _item in obj.get("input_descriptors")
                    ]
                    if obj.get("input_descriptors") is not None
                    else None
                ),
                "name": obj.get("name"),
                "purpose": obj.get("purpose"),
                "submission_requirements": (
                    [
                        SubmissionRequirements.from_dict(_item)
                        for _item in obj.get("submission_requirements")
                    ]
                    if obj.get("submission_requirements") is not None
                    else None
                ),
            }
        )
        return _obj
