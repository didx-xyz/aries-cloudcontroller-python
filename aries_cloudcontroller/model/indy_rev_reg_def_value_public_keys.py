# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.indy_rev_reg_def_value_public_keys_accum_key import (
    IndyRevRegDefValuePublicKeysAccumKey,
)


class IndyRevRegDefValuePublicKeys(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyRevRegDefValuePublicKeys - a model defined in OpenAPI
        accum_key: The accum_key of this IndyRevRegDefValuePublicKeys [Optional].
    """

    accum_key: Optional[IndyRevRegDefValuePublicKeysAccumKey] = Field(
        None, alias="accumKey"
    )

    class Config:
        allow_population_by_field_name = True


IndyRevRegDefValuePublicKeys.update_forward_refs()
