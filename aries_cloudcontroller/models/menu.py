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


from typing import List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from aries_cloudcontroller.models.menu_option import MenuOption
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Menu(BaseModel):
    """
    Menu
    """
    id: Optional[StrictStr] = Field(default=None, description="Message identifier", alias="@id")
    type: Optional[StrictStr] = Field(default=None, description="Message type", alias="@type")
    description: Optional[StrictStr] = Field(default=None, description="Introductory text for the menu")
    errormsg: Optional[StrictStr] = Field(default=None, description="An optional error message to display in menu header")
    options: List[MenuOption] = Field(description="List of menu options")
    title: Optional[StrictStr] = Field(default=None, description="Menu title")
    __properties: ClassVar[List[str]] = ["@id", "@type", "description", "errormsg", "options", "title"]

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
        """Create an instance of Menu from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                            "type",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item in self.options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['options'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of Menu from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "description": obj.get("description"),
            "errormsg": obj.get("errormsg"),
            "options": [MenuOption.from_dict(_item) for _item in obj.get("options")] if obj.get("options") is not None else None,
            "title": obj.get("title")
        })
        return _obj


