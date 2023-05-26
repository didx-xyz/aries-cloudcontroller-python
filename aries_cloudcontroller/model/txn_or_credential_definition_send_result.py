# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.credential_definition_send_result import (
    CredentialDefinitionSendResult,
)
from aries_cloudcontroller.model.transaction_record import TransactionRecord


class TxnOrCredentialDefinitionSendResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TxnOrCredentialDefinitionSendResult - a model defined in OpenAPI
        sent: The sent of this TxnOrCredentialDefinitionSendResult [Optional].
        txn: Credential definition transaction to endorse [Optional].
    """

    sent: Optional[CredentialDefinitionSendResult] = None
    txn: Optional[TransactionRecord] = None

    class Config:
        allow_population_by_field_name = True


TxnOrCredentialDefinitionSendResult.update_forward_refs()
