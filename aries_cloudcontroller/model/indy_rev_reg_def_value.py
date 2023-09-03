# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Literal, Optional, Union  # noqa: F401

from pydantic import (  # noqa: F401
    AnyUrl,
    BaseModel,
    ConfigDict,
    EmailStr,
    Extra,
    Field,
    field_validator,
)

from aries_cloudcontroller.model.indy_rev_reg_def_value_public_keys import (
    IndyRevRegDefValuePublicKeys,
)


class IndyRevRegDefValue(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyRevRegDefValue - a model defined in OpenAPI
        issuance_type: Issuance type [Optional].
        max_cred_num: Maximum number of credentials; registry size [Optional].
        public_keys: Public keys [Optional].
        tails_hash: Tails hash value [Optional].
        tails_location: Tails file location [Optional].
    """

    issuance_type: Optional[
        Literal["ISSUANCE_ON_DEMAND", "ISSUANCE_BY_DEFAULT"]
    ] = Field(None, alias="issuanceType")
    max_cred_num: Optional[int] = Field(None, alias="maxCredNum")
    public_keys: Optional[IndyRevRegDefValuePublicKeys] = Field(
        None, alias="publicKeys"
    )
    tails_hash: Optional[str] = Field(None, alias="tailsHash")
    tails_location: Optional[str] = Field(None, alias="tailsLocation")

    @field_validator("max_cred_num")
    @classmethod
    def max_cred_num_min(cls, value):
        # Property is optional
        if value is None:
            return

        if value < 1:
            raise ValueError(f"max_cred_num must be greater than 1, currently {value}")
        return value

    @field_validator("tails_hash")
    @classmethod
    def tails_hash_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = (
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$"
        )
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of tails_hash does not match regex pattern ('{pattern}')"
            )
        return value

    model_config = ConfigDict(populate_by_name=True)


IndyRevRegDefValue.model_rebuild()
