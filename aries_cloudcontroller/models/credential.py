# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.1.1b0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import orjson
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.linked_data_proof import LinkedDataProof
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class Credential(BaseModel):
    """
    Credential
    """  # noqa: E501

    # keep custom changes
    context: List[Union[str, Dict]] = Field(
        description="The JSON-LD context of the credential", alias="@context"
    )
    credential_status: Optional[Dict[str, Any]] = Field(
        default=None, alias="credentialStatus"
    )
    credential_subject: Dict[str, Any] = Field(alias="credentialSubject")
    expiration_date: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="The expiration date", alias="expirationDate"
    )
    id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="The ID of the credential"
    )
    issuance_date: Annotated[str, Field(strict=True)] = Field(
        description="The issuance date", alias="issuanceDate"
    )
    issuer: Union[str, Dict[str, Any]] = Field(
        description="The JSON-LD Verifiable Credential Issuer. Either string of object with id field."
    )
    proof: Optional[LinkedDataProof] = Field(
        default=None, description="The proof of the credential"
    )
    type: List[StrictStr] = Field(description="The JSON-LD type of the credential")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "@context",
        "credentialStatus",
        "credentialSubject",
        "expirationDate",
        "id",
        "issuanceDate",
        "issuer",
        "proof",
        "type",
    ]

    @field_validator("expiration_date")
    def expiration_date_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^([0-9]{4})-([0-9]{2})-([0-9]{2})([Tt ]([0-9]{2}):([0-9]{2}):([0-9]{2})(\.[0-9]+)?)?(([Zz]|([+-])([0-9]{2}):([0-9]{2})))?$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^([0-9]{4})-([0-9]{2})-([0-9]{2})([Tt ]([0-9]{2}):([0-9]{2}):([0-9]{2})(\.[0-9]+)?)?(([Zz]|([+-])([0-9]{2}):([0-9]{2})))?$/"
            )
        return value

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

    @field_validator("issuance_date")
    def issuance_date_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(
            r"^([0-9]{4})-([0-9]{2})-([0-9]{2})([Tt ]([0-9]{2}):([0-9]{2}):([0-9]{2})(\.[0-9]+)?)?(([Zz]|([+-])([0-9]{2}):([0-9]{2})))?$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^([0-9]{4})-([0-9]{2})-([0-9]{2})([Tt ]([0-9]{2}):([0-9]{2}):([0-9]{2})(\.[0-9]+)?)?(([Zz]|([+-])([0-9]{2}):([0-9]{2})))?$/"
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
        """Create an instance of Credential from a JSON string"""
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
        """Create an instance of Credential from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@context": obj.get("@context"),
                "credentialStatus": obj.get("credentialStatus"),
                "credentialSubject": obj.get("credentialSubject"),
                "expirationDate": obj.get("expirationDate"),
                "id": obj.get("id"),
                "issuanceDate": obj.get("issuanceDate"),
                "issuer": obj.get("issuer"),
                "proof": (
                    LinkedDataProof.from_dict(obj["proof"])
                    if obj.get("proof") is not None
                    else None
                ),
                "type": obj.get("type"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
