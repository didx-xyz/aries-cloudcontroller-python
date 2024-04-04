# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.menu_form import MenuForm
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class MenuOption(BaseModel):
    """
    MenuOption
    """  # noqa: E501

    description: Optional[StrictStr] = Field(
        default=None, description="Additional descriptive text for menu option"
    )
    disabled: Optional[StrictBool] = Field(
        default=None, description="Whether to show option as disabled"
    )
    form: Optional[MenuForm] = None
    name: StrictStr = Field(description="Menu option name (unique identifier)")
    title: StrictStr = Field(description="Menu option title")
    __properties: ClassVar[List[str]] = [
        "description",
        "disabled",
        "form",
        "name",
        "title",
    ]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MenuOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of form
        if self.form:
            _dict["form"] = self.form.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MenuOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "description": obj.get("description"),
                "disabled": obj.get("disabled"),
                "form": (
                    MenuForm.from_dict(obj.get("form"))
                    if obj.get("form") is not None
                    else None
                ),
                "name": obj.get("name"),
                "title": obj.get("title"),
            }
        )
        return _obj
