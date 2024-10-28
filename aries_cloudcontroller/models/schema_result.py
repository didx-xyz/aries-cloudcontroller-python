# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.1.1b0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.schema_state import SchemaState
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class SchemaResult(BaseModel):
    """
    SchemaResult
    """  # noqa: E501

    job_id: Optional[StrictStr] = None
    registration_metadata: Optional[Dict[str, Any]] = None
    schema_metadata: Optional[Dict[str, Any]] = None
    schema_state: Optional[SchemaState] = None
    __properties: ClassVar[List[str]] = [
        "job_id",
        "registration_metadata",
        "schema_metadata",
        "schema_state",
    ]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SchemaResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of schema_state
        if self.schema_state:
            _dict["schema_state"] = self.schema_state.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SchemaResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "job_id": obj.get("job_id"),
                "registration_metadata": obj.get("registration_metadata"),
                "schema_metadata": obj.get("schema_metadata"),
                "schema_state": (
                    SchemaState.from_dict(obj["schema_state"])
                    if obj.get("schema_state") is not None
                    else None
                ),
            }
        )
        return _obj
