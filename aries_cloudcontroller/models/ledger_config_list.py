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


from typing import List
from pydantic import BaseModel
from aries_cloudcontroller.models.ledger_config_instance import LedgerConfigInstance
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LedgerConfigList(BaseModel):
    """
    LedgerConfigList
    """
    ledger_config_list: List[LedgerConfigInstance]
    __properties: ClassVar[List[str]] = ["ledger_config_list"]

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
        """Create an instance of LedgerConfigList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ledger_config_list (list)
        _items = []
        if self.ledger_config_list:
            for _item in self.ledger_config_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ledger_config_list'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of LedgerConfigList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ledger_config_list": [LedgerConfigInstance.from_dict(_item) for _item in obj.get("ledger_config_list")] if obj.get("ledger_config_list") is not None else None
        })
        return _obj


