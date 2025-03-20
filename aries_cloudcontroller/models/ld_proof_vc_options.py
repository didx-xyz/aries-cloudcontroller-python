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
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.credential_status_options import (
    CredentialStatusOptions,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class LDProofVCOptions(BaseModel):
    """
    LDProofVCOptions
    """  # noqa: E501

    challenge: Optional[StrictStr] = Field(
        default=None,
        description="A challenge to include in the proof. SHOULD be provided by the requesting party of the credential (=holder)",
    )
    created: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="The date and time of the proof (with a maximum accuracy in seconds). Defaults to current system time",
    )
    credential_status: Optional[CredentialStatusOptions] = Field(
        default=None,
        description="The credential status mechanism to use for the credential. Omitting the property indicates the issued credential will not include a credential status",
        alias="credentialStatus",
    )
    domain: Optional[StrictStr] = Field(
        default=None, description="The intended domain of validity for the proof"
    )
    proof_purpose: Optional[StrictStr] = Field(
        default=None,
        description="The proof purpose used for the proof. Should match proof purposes registered in the Linked Data Proofs Specification",
        alias="proofPurpose",
    )
    proof_type: Optional[StrictStr] = Field(
        default=None,
        description="The proof type used for the proof. Should match suites registered in the Linked Data Cryptographic Suite Registry",
        alias="proofType",
    )
    verification_method: Optional[StrictStr] = Field(
        default=None,
        description="The verification method to use for the proof. Should match a verification method in the wallet",
        alias="verificationMethod",
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "challenge",
        "created",
        "credentialStatus",
        "domain",
        "proofPurpose",
        "proofType",
        "verificationMethod",
    ]

    @field_validator("created")
    def created_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$/"
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
        """Create an instance of LDProofVCOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credential_status
        if self.credential_status:
            _dict["credentialStatus"] = self.credential_status.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LDProofVCOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "challenge": obj.get("challenge"),
                "created": obj.get("created"),
                "credentialStatus": (
                    CredentialStatusOptions.from_dict(obj["credentialStatus"])
                    if obj.get("credentialStatus") is not None
                    else None
                ),
                "domain": obj.get("domain"),
                "proofPurpose": obj.get("proofPurpose"),
                "proofType": obj.get("proofType"),
                "verificationMethod": obj.get("verificationMethod"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
