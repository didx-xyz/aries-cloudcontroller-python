# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.filter import Filter


class DIFField(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DIFField - a model defined in OpenAPI
        filter: The filter of this DIFField [Optional].
        id: ID [Optional].
        path: The path of this DIFField [Optional].
        predicate: Preference [Optional].
        purpose: Purpose [Optional].
    """

    filter: Optional[Filter] = None
    id: Optional[str] = None
    path: Optional[List[str]] = None
    predicate: Optional[Literal["required", "preferred"]] = None
    purpose: Optional[str] = None

    def __init__(
        self,
        *,
        filter: Optional[Filter] = None,
        id: Optional[str] = None,
        path: Optional[List[str]] = None,
        predicate: Optional[Literal["required", "preferred"]] = None,
        purpose: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            filter=filter,
            id=id,
            path=path,
            predicate=predicate,
            purpose=purpose,
            **kwargs,
        )


DIFField.update_forward_refs()
