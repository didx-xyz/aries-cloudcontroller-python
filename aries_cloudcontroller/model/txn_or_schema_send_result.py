# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.schema_send_result import SchemaSendResult
from aries_cloudcontroller.model.transaction_record import TransactionRecord


class TxnOrSchemaSendResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TxnOrSchemaSendResult - a model defined in OpenAPI
        sent: Content sent [Optional].
        txn: Schema transaction to endorse [Optional].
    """

    sent: Optional[SchemaSendResult] = None
    txn: Optional[TransactionRecord] = None
    model_config = ConfigDict(populate_by_name=True)


TxnOrSchemaSendResult.update_forward_refs()
