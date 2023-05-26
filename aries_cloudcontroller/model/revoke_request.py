# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class RevokeRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RevokeRequest - a model defined in OpenAPI
        comment: Optional comment to include in revocation notification [Optional].
        connection_id: Connection ID to which the revocation notification will be sent; required if notify is true [Optional].
        cred_ex_id: Credential exchange identifier [Optional].
        cred_rev_id: Credential revocation identifier [Optional].
        notify: Send a notification to the credential recipient [Optional].
        notify_version: Specify which version of the revocation notification should be sent [Optional].
        publish: (True) publish revocation to ledger immediately, or (default, False) mark it pending [Optional].
        rev_reg_id: Revocation registry identifier [Optional].
        thread_id: Thread ID of the credential exchange message thread resulting in the credential now being revoked; required if notify is true [Optional].
    """

    comment: Optional[str] = None
    connection_id: Optional[str] = None
    cred_ex_id: Optional[str] = None
    cred_rev_id: Optional[str] = None
    notify: Optional[bool] = None
    notify_version: Optional[Literal["v1_0", "v2_0"]] = None
    publish: Optional[bool] = None
    rev_reg_id: Optional[str] = None
    thread_id: Optional[str] = None

    @validator("connection_id")
    def connection_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of connection_id does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("cred_ex_id")
    def cred_ex_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of cred_ex_id does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("cred_rev_id")
    def cred_rev_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[1-9][0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of cred_rev_id does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("rev_reg_id")
    def rev_reg_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of rev_reg_id does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


RevokeRequest.update_forward_refs()
