# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.ledger_config_instance import LedgerConfigInstance


class LedgerConfigList(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LedgerConfigList - a model defined in OpenAPI
        ledger_config_list: The ledger_config_list of this LedgerConfigList.
    """

    ledger_config_list: List[LedgerConfigInstance]
    model_config = ConfigDict(populate_by_name=True)


LedgerConfigList.update_forward_refs()
