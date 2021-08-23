# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class CredDefValueRevocation(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredDefValueRevocation - a model defined in OpenAPI
        g: The g of this CredDefValueRevocation [Optional].
        g_dash: The g_dash of this CredDefValueRevocation [Optional].
        h: The h of this CredDefValueRevocation [Optional].
        h0: The h0 of this CredDefValueRevocation [Optional].
        h1: The h1 of this CredDefValueRevocation [Optional].
        h2: The h2 of this CredDefValueRevocation [Optional].
        h_cap: The h_cap of this CredDefValueRevocation [Optional].
        htilde: The htilde of this CredDefValueRevocation [Optional].
        pk: The pk of this CredDefValueRevocation [Optional].
        u: The u of this CredDefValueRevocation [Optional].
        y: The y of this CredDefValueRevocation [Optional].
    """

    g: Optional[str] = None
    g_dash: Optional[str] = None
    h: Optional[str] = None
    h0: Optional[str] = None
    h1: Optional[str] = None
    h2: Optional[str] = None
    h_cap: Optional[str] = None
    htilde: Optional[str] = None
    pk: Optional[str] = None
    u: Optional[str] = None
    y: Optional[str] = None

    def __init__(
        self,
        *,
        g: Optional[str] = None,
        g_dash: Optional[str] = None,
        h: Optional[str] = None,
        h0: Optional[str] = None,
        h1: Optional[str] = None,
        h2: Optional[str] = None,
        h_cap: Optional[str] = None,
        htilde: Optional[str] = None,
        pk: Optional[str] = None,
        u: Optional[str] = None,
        y: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            g=g,
            g_dash=g_dash,
            h=h,
            h0=h0,
            h1=h1,
            h2=h2,
            h_cap=h_cap,
            htilde=htilde,
            pk=pk,
            u=u,
            y=y,
            **kwargs,
        )


CredDefValueRevocation.update_forward_refs()
