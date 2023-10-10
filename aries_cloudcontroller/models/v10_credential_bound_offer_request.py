# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from aries_cloudcontroller.models.credential_proposal import CredentialProposal
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V10CredentialBoundOfferRequest(BaseModel):
    """
    V10CredentialBoundOfferRequest
    """
    counter_proposal: Optional[CredentialProposal] = None
    __properties: ClassVar[List[str]] = ["counter_proposal"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.model_dump_json(self.to_dict(), by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V10CredentialBoundOfferRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of counter_proposal
        if self.counter_proposal:
            _dict['counter_proposal'] = self.counter_proposal.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of V10CredentialBoundOfferRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "counter_proposal": CredentialProposal.from_dict(obj.get("counter_proposal")) if obj.get("counter_proposal") is not None else None
        })
        return _obj


