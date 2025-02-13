# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.2.1.post20250213
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.linked_data_proof import LinkedDataProof
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class VerifiablePresentation(BaseModel):
    """
    VerifiablePresentation
    """  # noqa: E501

    context: List[Dict[str, Any]] = Field(
        description="The JSON-LD context of the presentation", alias="@context"
    )
    holder: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The JSON-LD Verifiable Credential Holder. Either string of object with id field.",
    )
    id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="The ID of the presentation"
    )
    proof: LinkedDataProof = Field(description="The proof of the presentation")
    type: List[StrictStr] = Field(description="The JSON-LD type of the presentation")
    verifiable_credential: Optional[List[Dict[str, Any]]] = Field(
        default=None, alias="verifiableCredential"
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "@context",
        "holder",
        "id",
        "proof",
        "type",
        "verifiableCredential",
    ]

    @field_validator("id")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"\w+:(\/?\/?)[^\s]+", value):
            raise ValueError(
                r"must validate the regular expression /\w+:(\/?\/?)[^\s]+/"
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
        """Create an instance of VerifiablePresentation from a JSON string"""
        return cls.from_dict(orjson.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set(
            [
                "additional_properties",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of proof
        if self.proof:
            _dict["proof"] = self.proof.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VerifiablePresentation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@context": obj.get("@context"),
                "holder": obj.get("holder"),
                "id": obj.get("id"),
                "proof": (
                    LinkedDataProof.from_dict(obj["proof"])
                    if obj.get("proof") is not None
                    else None
                ),
                "type": obj.get("type"),
                "verifiableCredential": obj.get("verifiableCredential"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
