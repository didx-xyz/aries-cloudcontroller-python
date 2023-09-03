# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import (
    ConfigDict,
    AnyUrl,
    BaseModel,
    EmailStr,
    validator,
    Field,
    Extra,
)  # noqa: F401
from aries_cloudcontroller.model.publish_revocations import PublishRevocations
from aries_cloudcontroller.model.transaction_record import TransactionRecord


class TxnOrPublishRevocationsResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TxnOrPublishRevocationsResult - a model defined in OpenAPI
        sent: The sent of this TxnOrPublishRevocationsResult [Optional].
        txn: Revocation registry revocations transaction to endorse [Optional].
    """

    sent: Optional[PublishRevocations] = None
    txn: Optional[TransactionRecord] = None
    model_config = ConfigDict(populate_by_name=True)


TxnOrPublishRevocationsResult.model_rebuild()
