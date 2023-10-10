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


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VCRecord(BaseModel):
    """
    VCRecord
    """
    contexts: Optional[List[Annotated[str, Field(strict=True)]]] = None
    cred_tags: Optional[Dict[str, StrictStr]] = None
    cred_value: Optional[Union[str, Any]] = Field(default=None, description="(JSON-serializable) credential value")
    expanded_types: Optional[List[StrictStr]] = None
    given_id: Optional[StrictStr] = Field(default=None, description="Credential identifier")
    issuer_id: Optional[StrictStr] = Field(default=None, description="Issuer identifier")
    proof_types: Optional[List[StrictStr]] = None
    record_id: Optional[StrictStr] = Field(default=None, description="Record identifier")
    schema_ids: Optional[List[StrictStr]] = None
    subject_ids: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["contexts", "cred_tags", "cred_value", "expanded_types", "given_id", "issuer_id", "proof_types", "record_id", "schema_ids", "subject_ids"]

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
        """Create an instance of VCRecord from a JSON string"""
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
        """Create an instance of VCRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contexts": obj.get("contexts"),
            "cred_tags": obj.get("cred_tags"),
            "cred_value": obj.get("cred_value"),
            "expanded_types": obj.get("expanded_types"),
            "given_id": obj.get("given_id"),
            "issuer_id": obj.get("issuer_id"),
            "proof_types": obj.get("proof_types"),
            "record_id": obj.get("record_id"),
            "schema_ids": obj.get("schema_ids"),
            "subject_ids": obj.get("subject_ids")
        })
        return _obj


