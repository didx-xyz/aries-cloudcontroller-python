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


from typing import Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class W3CCredentialsListRequest(BaseModel):
    """
    W3CCredentialsListRequest
    """
    contexts: Optional[List[Annotated[str, Field(strict=True)]]] = None
    given_id: Optional[StrictStr] = Field(default=None, description="Given credential id to match")
    issuer_id: Optional[StrictStr] = Field(default=None, description="Credential issuer identifier to match")
    max_results: Optional[StrictInt] = Field(default=None, description="Maximum number of results to return")
    proof_types: Optional[List[StrictStr]] = None
    schema_ids: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Schema identifiers, all of which to match")
    subject_ids: Optional[List[StrictStr]] = Field(default=None, description="Subject identifiers, all of which to match")
    tag_query: Optional[Dict[str, StrictStr]] = Field(default=None, description="Tag filter")
    types: Optional[List[Annotated[str, Field(strict=True)]]] = None
    __properties: ClassVar[List[str]] = ["contexts", "given_id", "issuer_id", "max_results", "proof_types", "schema_ids", "subject_ids", "tag_query", "types"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of W3CCredentialsListRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of W3CCredentialsListRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contexts": obj.get("contexts"),
            "given_id": obj.get("given_id"),
            "issuer_id": obj.get("issuer_id"),
            "max_results": obj.get("max_results"),
            "proof_types": obj.get("proof_types"),
            "schema_ids": obj.get("schema_ids"),
            "subject_ids": obj.get("subject_ids"),
            "tag_query": obj.get("tag_query"),
            "types": obj.get("types")
        })
        return _obj


