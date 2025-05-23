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

from aries_cloudcontroller.models.cred_def_post_options import CredDefPostOptions
from aries_cloudcontroller.models.inner_cred_def import InnerCredDef
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class CredDefPostRequest(BaseModel):
    """
    CredDefPostRequest
    """  # noqa: E501

    credential_definition: Optional[InnerCredDef] = None
    options: Optional[CredDefPostOptions] = None
    __properties: ClassVar[List[str]] = ["credential_definition", "options"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CredDefPostRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credential_definition
        if self.credential_definition:
            _dict["credential_definition"] = self.credential_definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict["options"] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CredDefPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "credential_definition": (
                    InnerCredDef.from_dict(obj["credential_definition"])
                    if obj.get("credential_definition") is not None
                    else None
                ),
                "options": (
                    CredDefPostOptions.from_dict(obj["options"])
                    if obj.get("options") is not None
                    else None
                ),
            }
        )
        return _obj
