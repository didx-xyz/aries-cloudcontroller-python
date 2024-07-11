from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import Field
from typing_extensions import Self

from aries_cloudcontroller.models.wallet_record import WalletRecord


class WalletRecordWithGroups(WalletRecord):
    group_id: Optional[str] = Field(None, examples=["SomeGroupId"])

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WalletRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "created_at": obj.get("created_at"),
                "key_management_mode": obj.get("key_management_mode"),
                "settings": obj.get("settings"),
                "state": obj.get("state"),
                "updated_at": obj.get("updated_at"),
                "wallet_id": obj.get("wallet_id"),
                "group_id": obj.get("group_id"),
            }
        )
        return _obj
