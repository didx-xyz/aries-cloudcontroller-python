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

from aries_cloudcontroller.models.indy_rev_reg_def import IndyRevRegDef
from aries_cloudcontroller.models.indy_rev_reg_entry import IndyRevRegEntry
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class IssuerRevRegRecord(BaseModel):
    """
    IssuerRevRegRecord
    """  # noqa: E501

    created_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of record creation"
    )
    cred_def_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Credential definition identifier"
    )
    error_msg: Optional[StrictStr] = Field(default=None, description="Error message")
    issuer_did: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Issuer DID"
    )
    max_cred_num: Optional[StrictInt] = Field(
        default=None,
        description="Maximum number of credentials for revocation registry",
    )
    pending_pub: Optional[List[StrictStr]] = Field(
        default=None,
        description="Credential revocation identifier for credential revoked and pending publication to ledger",
    )
    record_id: Optional[StrictStr] = Field(
        default=None, description="Issuer revocation registry record identifier"
    )
    revoc_def_type: Optional[StrictStr] = Field(
        default=None, description="Revocation registry type (specify CL_ACCUM)"
    )
    revoc_reg_def: Optional[IndyRevRegDef] = Field(
        default=None, description="Revocation registry definition"
    )
    revoc_reg_entry: Optional[IndyRevRegEntry] = Field(
        default=None, description="Revocation registry entry"
    )
    revoc_reg_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Revocation registry identifier"
    )
    state: Optional[StrictStr] = Field(
        default=None, description="Issue revocation registry record state"
    )
    tag: Optional[StrictStr] = Field(
        default=None, description="Tag within issuer revocation registry identifier"
    )
    tails_hash: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Tails hash"
    )
    tails_local_path: Optional[StrictStr] = Field(
        default=None, description="Local path to tails file"
    )
    tails_public_uri: Optional[StrictStr] = Field(
        default=None, description="Public URI for tails file"
    )
    updated_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of last record update"
    )
    __properties: ClassVar[List[str]] = [
        "created_at",
        "cred_def_id",
        "error_msg",
        "issuer_did",
        "max_cred_num",
        "pending_pub",
        "record_id",
        "revoc_def_type",
        "revoc_reg_def",
        "revoc_reg_entry",
        "revoc_reg_id",
        "state",
        "tag",
        "tails_hash",
        "tails_local_path",
        "tails_public_uri",
        "updated_at",
    ]

    @field_validator("created_at")
    def created_at_validate_regular_expression(cls, value):
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

    @field_validator("cred_def_id")
    def cred_def_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$/"
            )
        return value

    @field_validator("issuer_did")
    def issuer_did_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/"
            )
        return value

    @field_validator("revoc_def_type")
    def revoc_def_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["CL_ACCUM"]):
            raise ValueError("must be one of enum values ('CL_ACCUM')")
        return value

    @field_validator("revoc_reg_id")
    def revoc_reg_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)/"
            )
        return value

    @field_validator("tails_hash")
    def tails_hash_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$/"
            )
        return value

    @field_validator("updated_at")
    def updated_at_validate_regular_expression(cls, value):
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
        """Create an instance of IssuerRevRegRecord from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of revoc_reg_def
        if self.revoc_reg_def:
            _dict["revoc_reg_def"] = self.revoc_reg_def.to_dict()
        # override the default output from pydantic by calling `to_dict()` of revoc_reg_entry
        if self.revoc_reg_entry:
            _dict["revoc_reg_entry"] = self.revoc_reg_entry.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IssuerRevRegRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "created_at": obj.get("created_at"),
                "cred_def_id": obj.get("cred_def_id"),
                "error_msg": obj.get("error_msg"),
                "issuer_did": obj.get("issuer_did"),
                "max_cred_num": obj.get("max_cred_num"),
                "pending_pub": obj.get("pending_pub"),
                "record_id": obj.get("record_id"),
                "revoc_def_type": obj.get("revoc_def_type"),
                "revoc_reg_def": (
                    IndyRevRegDef.from_dict(obj["revoc_reg_def"])
                    if obj.get("revoc_reg_def") is not None
                    else None
                ),
                "revoc_reg_entry": (
                    IndyRevRegEntry.from_dict(obj["revoc_reg_entry"])
                    if obj.get("revoc_reg_entry") is not None
                    else None
                ),
                "revoc_reg_id": obj.get("revoc_reg_id"),
                "state": obj.get("state"),
                "tag": obj.get("tag"),
                "tails_hash": obj.get("tails_hash"),
                "tails_local_path": obj.get("tails_local_path"),
                "tails_public_uri": obj.get("tails_public_uri"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
