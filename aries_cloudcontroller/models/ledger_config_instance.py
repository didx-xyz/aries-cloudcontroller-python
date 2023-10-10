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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LedgerConfigInstance(BaseModel):
    """
    LedgerConfigInstance
    """
    genesis_file: Optional[StrictStr] = Field(default=None, description="genesis_file")
    genesis_transactions: Optional[StrictStr] = Field(default=None, description="genesis_transactions")
    genesis_url: Optional[StrictStr] = Field(default=None, description="genesis_url")
    id: Optional[StrictStr] = Field(default=None, description="ledger_id")
    is_production: Optional[StrictBool] = Field(default=None, description="is_production")
    __properties: ClassVar[List[str]] = ["genesis_file", "genesis_transactions", "genesis_url", "id", "is_production"]

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
        """Create an instance of LedgerConfigInstance from a JSON string"""
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
        """Create an instance of LedgerConfigInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "genesis_file": obj.get("genesis_file"),
            "genesis_transactions": obj.get("genesis_transactions"),
            "genesis_url": obj.get("genesis_url"),
            "id": obj.get("id"),
            "is_production": obj.get("is_production")
        })
        return _obj

