# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.12.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.attach_decorator_data import AttachDecoratorData
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class AttachDecorator(BaseModel):
    """
    AttachDecorator
    """  # noqa: E501

    id: Optional[StrictStr] = Field(
        default=None, description="Attachment identifier", alias="@id"
    )
    byte_count: Optional[StrictInt] = Field(
        default=None, description="Byte count of data included by reference"
    )
    data: AttachDecoratorData
    description: Optional[StrictStr] = Field(
        default=None, description="Human-readable description of content"
    )
    filename: Optional[StrictStr] = Field(default=None, description="File name")
    lastmod_time: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="Hint regarding last modification datetime, in ISO-8601 format",
    )
    mime_type: Optional[StrictStr] = Field(
        default=None, description="MIME type", alias="mime-type"
    )
    __properties: ClassVar[List[str]] = [
        "@id",
        "byte_count",
        "data",
        "description",
        "filename",
        "lastmod_time",
        "mime-type",
    ]

    @field_validator("lastmod_time")
    def lastmod_time_validate_regular_expression(cls, value):
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
        """Create an instance of AttachDecorator from a JSON string"""
        return cls.from_dict(json.loads(json_str))

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
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict["data"] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AttachDecorator from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@id": obj.get("@id"),
                "byte_count": obj.get("byte_count"),
                "data": (
                    AttachDecoratorData.from_dict(obj["data"])
                    if obj.get("data") is not None
                    else None
                ),
                "description": obj.get("description"),
                "filename": obj.get("filename"),
                "lastmod_time": obj.get("lastmod_time"),
                "mime-type": obj.get("mime-type"),
            }
        )
        return _obj
