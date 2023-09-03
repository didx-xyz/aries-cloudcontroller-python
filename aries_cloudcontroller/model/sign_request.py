# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.doc import Doc


class SignRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SignRequest - a model defined in OpenAPI
        doc: The doc of this SignRequest.
        verkey: Verkey to use for signing.
    """

    doc: Doc
    verkey: str
    model_config = ConfigDict(populate_by_name=True)


SignRequest.update_forward_refs()
