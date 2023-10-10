# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated

from aries_cloudcontroller.models.linked_data_proof import LinkedDataProof

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Credential(BaseModel):
    """
    Credential
    """

    context: List[Union[str, Any]] = Field(
        description="The JSON-LD context of the credential", alias="@context"
    )
    credential_subject: Union[str, Any] = Field(alias="credentialSubject")
    expiration_date: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="The expiration date", alias="expirationDate"
    )
    id: Optional[Annotated[str, Field(strict=True)]] = None
    issuance_date: Annotated[str, Field(strict=True)] = Field(
        description="The issuance date", alias="issuanceDate"
    )
    issuer: Union[str, Any] = Field(
        description="The JSON-LD Verifiable Credential Issuer. Either string of object with id field."
    )
    proof: Optional[LinkedDataProof] = None
    type: List[StrictStr] = Field(description="The JSON-LD type of the credential")
    __properties: ClassVar[List[str]] = [
        "@context",
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

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Credential from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of proof
        if self.proof:
            _dict["proof"] = self.proof.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of Credential from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@context": obj.get("@context"),
                "credentialSubject": obj.get("credentialSubject"),
                "expirationDate": obj.get("expirationDate"),
                "id": obj.get("id"),
                "issuanceDate": obj.get("issuanceDate"),
                "issuer": obj.get("issuer"),
                "proof": LinkedDataProof.from_dict(obj.get("proof"))
                if obj.get("proof") is not None
                else None,
                "type": obj.get("type"),
            }
        )
        return _obj
