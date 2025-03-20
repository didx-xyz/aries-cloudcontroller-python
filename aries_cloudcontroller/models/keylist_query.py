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
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.keylist_query_paginate import KeylistQueryPaginate
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class KeylistQuery(BaseModel):
    """
    KeylistQuery
    """  # noqa: E501

    id: Optional[StrictStr] = Field(
        default=None, description="Message identifier", alias="@id"
    )
    type: Optional[StrictStr] = Field(
        default=None, description="Message type", alias="@type"
    )
    filter: Optional[Dict[str, Any]] = Field(
        default=None, description="Query dictionary object"
    )
    paginate: Optional[KeylistQueryPaginate] = Field(
        default=None, description="Pagination info"
    )
    __properties: ClassVar[List[str]] = ["@id", "@type", "filter", "paginate"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of KeylistQuery from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of paginate
        if self.paginate:
            _dict["paginate"] = self.paginate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeylistQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@id": obj.get("@id"),
                "@type": obj.get("@type"),
                "filter": obj.get("filter"),
                "paginate": (
                    KeylistQueryPaginate.from_dict(obj["paginate"])
                    if obj.get("paginate") is not None
                    else None
                ),
            }
        )
        return _obj
