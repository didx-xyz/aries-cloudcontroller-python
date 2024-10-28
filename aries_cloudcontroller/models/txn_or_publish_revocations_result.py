# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.1.1b0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import orjson
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.transaction_record import TransactionRecord
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class TxnOrPublishRevocationsResult(BaseModel):
    """
    TxnOrPublishRevocationsResult
    """  # noqa: E501

    rrid2crid: Optional[Dict[str, List[Annotated[str, Field(strict=True)]]]] = Field(
        default=None, description="Credential revocation ids by revocation registry id"
    )
    txn: Optional[List[TransactionRecord]] = None
    __properties: ClassVar[List[str]] = ["rrid2crid", "txn"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TxnOrPublishRevocationsResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in txn (list)
        _items = []
        if self.txn:
            for _item_txn in self.txn:
                if _item_txn:
                    _items.append(_item_txn.to_dict())
            _dict["txn"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TxnOrPublishRevocationsResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "rrid2crid": obj.get("rrid2crid"),
                "txn": (
                    [TransactionRecord.from_dict(_item) for _item in obj["txn"]]
                    if obj.get("txn") is not None
                    else None
                ),
            }
        )
        return _obj
