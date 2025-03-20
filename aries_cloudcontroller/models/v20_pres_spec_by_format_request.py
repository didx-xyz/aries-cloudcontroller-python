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
from pydantic import BaseModel, Field, StrictBool
from typing_extensions import Self

from aries_cloudcontroller.models.dif_pres_spec import DIFPresSpec
from aries_cloudcontroller.models.indy_pres_spec import IndyPresSpec
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class V20PresSpecByFormatRequest(BaseModel):
    """
    V20PresSpecByFormatRequest
    """  # noqa: E501

    anoncreds: Optional[IndyPresSpec] = Field(
        default=None, description="Presentation specification for anoncreds"
    )
    auto_remove: Optional[StrictBool] = Field(
        default=None,
        description="Whether to remove the presentation exchange record on completion (overrides --preserve-exchange-records configuration setting)",
    )
    dif: Optional[DIFPresSpec] = Field(
        default=None,
        description="Optional Presentation specification for DIF, overrides the PresentationExchange record's PresRequest",
    )
    indy: Optional[IndyPresSpec] = Field(
        default=None, description="Presentation specification for indy"
    )
    trace: Optional[StrictBool] = Field(
        default=None,
        description="Record trace information, based on agent configuration",
    )
    __properties: ClassVar[List[str]] = [
        "anoncreds",
        "auto_remove",
        "dif",
        "indy",
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
        """Create an instance of V20PresSpecByFormatRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of anoncreds
        if self.anoncreds:
            _dict["anoncreds"] = self.anoncreds.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dif
        if self.dif:
            _dict["dif"] = self.dif.to_dict()
        # override the default output from pydantic by calling `to_dict()` of indy
        if self.indy:
            _dict["indy"] = self.indy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V20PresSpecByFormatRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "anoncreds": (
                    IndyPresSpec.from_dict(obj["anoncreds"])
                    if obj.get("anoncreds") is not None
                    else None
                ),
                "auto_remove": obj.get("auto_remove"),
                "dif": (
                    DIFPresSpec.from_dict(obj["dif"])
                    if obj.get("dif") is not None
                    else None
                ),
                "indy": (
                    IndyPresSpec.from_dict(obj["indy"])
                    if obj.get("indy") is not None
                    else None
                ),
                "trace": obj.get("trace"),
            }
        )
        return _obj
