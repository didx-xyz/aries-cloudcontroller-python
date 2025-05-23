# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.3.0.post20250507
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel
from typing_extensions import Self

from aries_cloudcontroller.models.dif_options import DIFOptions
from aries_cloudcontroller.models.input_descriptors import InputDescriptors
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class DIFProofProposal(BaseModel):
    """
    DIFProofProposal
    """  # noqa: E501

    input_descriptors: Optional[List[InputDescriptors]] = None
    options: Optional[DIFOptions] = None
    __properties: ClassVar[List[str]] = ["input_descriptors", "options"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DIFProofProposal from a JSON string"""
        return cls.from_dict(orjson.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in input_descriptors (list)
        _items = []
        if self.input_descriptors:
            for _item_input_descriptors in self.input_descriptors:
                if _item_input_descriptors:
                    _items.append(_item_input_descriptors.to_dict())
            _dict["input_descriptors"] = _items
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict["options"] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DIFProofProposal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "input_descriptors": (
                    [
                        InputDescriptors.from_dict(_item)
                        for _item in obj["input_descriptors"]
                    ]
                    if obj.get("input_descriptors") is not None
                    else None
                ),
                "options": (
                    DIFOptions.from_dict(obj["options"])
                    if obj.get("options") is not None
                    else None
                ),
            }
        )
        return _obj
