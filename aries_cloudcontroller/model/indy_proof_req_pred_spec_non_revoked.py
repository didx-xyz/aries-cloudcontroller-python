# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field, Extra  # noqa: F401


class IndyProofReqPredSpecNonRevoked(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofReqPredSpecNonRevoked - a model defined in OpenAPI
        from_: Earliest time of interest in non-revocation interval [Optional].
        to: Latest time of interest in non-revocation interval [Optional].
    """

    from_: Optional[int] = Field(None, alias="from")
    to: Optional[int] = None

    @field_validator("from_")
    @classmethod
    def from__max(cls, value):
        # Property is optional
        if value is None:
            return

        if value > 18446744073709551615:
            raise ValueError(
                f"from_ must be less than 18446744073709551615, currently {value}"
            )
        return value

    @field_validator("from_")
    @classmethod
    def from__min(cls, value):
        # Property is optional
        if value is None:
            return

        if value < 0:
            raise ValueError(f"from_ must be greater than 0, currently {value}")
        return value

    @field_validator("to")
    @classmethod
    def to_max(cls, value):
        # Property is optional
        if value is None:
            return

        if value > 18446744073709551615:
            raise ValueError(
                f"to must be less than 18446744073709551615, currently {value}"
            )
        return value

    @field_validator("to")
    @classmethod
    def to_min(cls, value):
        # Property is optional
        if value is None:
            return

        if value < 0:
            raise ValueError(f"to must be greater than 0, currently {value}")
        return value
    model_config = ConfigDict(populate_by_name=True)


IndyProofReqPredSpecNonRevoked.update_forward_refs()
