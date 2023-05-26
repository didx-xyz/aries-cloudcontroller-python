# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class W3CCredentialsListRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    W3CCredentialsListRequest - a model defined in OpenAPI
        contexts: The contexts of this W3CCredentialsListRequest [Optional].
        given_id: Given credential id to match [Optional].
        issuer_id: Credential issuer identifier to match [Optional].
        max_results: Maximum number of results to return [Optional].
        proof_types: The proof_types of this W3CCredentialsListRequest [Optional].
        schema_ids: Schema identifiers, all of which to match [Optional].
        subject_ids: Subject identifiers, all of which to match [Optional].
        tag_query: Tag filter [Optional].
        types: The types of this W3CCredentialsListRequest [Optional].
    """

    contexts: Optional[List[str]] = None
    given_id: Optional[str] = None
    issuer_id: Optional[str] = None
    max_results: Optional[int] = None
    proof_types: Optional[List[str]] = None
    schema_ids: Optional[List[str]] = None
    subject_ids: Optional[List[str]] = None
    tag_query: Optional[Dict[str, str]] = None
    types: Optional[List[str]] = None

    class Config:
        allow_population_by_field_name = True


W3CCredentialsListRequest.update_forward_refs()
