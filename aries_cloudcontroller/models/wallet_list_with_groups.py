from __future__ import annotations

from typing import Any, Dict, List, Optional

from typing_extensions import Self

from aries_cloudcontroller.models.wallet_list import WalletList
from aries_cloudcontroller.models.wallet_record_with_groups import (
    WalletRecordWithGroups,
)


class WalletListWithGroups(WalletList):
    results: Optional[List[WalletRecordWithGroups]] = None

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WalletListWithGroups from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "results": (
                    [
                        WalletRecordWithGroups.from_dict(_item)
                        for _item in obj["results"]
                    ]
                    if obj.get("results") is not None
                    else None
                )
            }
        )
        return _obj
