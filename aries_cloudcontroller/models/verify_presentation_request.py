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

from pydantic import BaseModel, Field
from typing_extensions import Self

from aries_cloudcontroller.models.ld_proof_vc_options import LDProofVCOptions
from aries_cloudcontroller.models.verifiable_presentation import VerifiablePresentation
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class VerifyPresentationRequest(BaseModel):
    """
    VerifyPresentationRequest
    """  # noqa: E501

    options: Optional[LDProofVCOptions] = None
    verifiable_presentation: Optional[VerifiablePresentation] = Field(
        default=None, alias="verifiablePresentation"
    )
    __properties: ClassVar[List[str]] = ["options", "verifiablePresentation"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of VerifyPresentationRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict["options"] = self.options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verifiable_presentation
        if self.verifiable_presentation:
            _dict["verifiablePresentation"] = self.verifiable_presentation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VerifyPresentationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "options": (
                    LDProofVCOptions.from_dict(obj["options"])
                    if obj.get("options") is not None
                    else None
                ),
                "verifiablePresentation": (
                    VerifiablePresentation.from_dict(obj["verifiablePresentation"])
                    if obj.get("verifiablePresentation") is not None
                    else None
                ),
            }
        )
        return _obj
