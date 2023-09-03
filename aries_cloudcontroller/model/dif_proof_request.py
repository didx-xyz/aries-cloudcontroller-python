# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.dif_options import DIFOptions
from aries_cloudcontroller.model.presentation_definition import PresentationDefinition


class DIFProofRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DIFProofRequest - a model defined in OpenAPI
        presentation_definition: The presentation_definition of this DIFProofRequest.
        options: The options of this DIFProofRequest [Optional].
    """

    presentation_definition: PresentationDefinition
    options: Optional[DIFOptions] = None
    model_config = ConfigDict(populate_by_name=True)


DIFProofRequest.update_forward_refs()
