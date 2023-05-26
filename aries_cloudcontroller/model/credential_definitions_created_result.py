# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class CredentialDefinitionsCreatedResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredentialDefinitionsCreatedResult - a model defined in OpenAPI
        credential_definition_ids: The credential_definition_ids of this CredentialDefinitionsCreatedResult [Optional].
    """

    credential_definition_ids: Optional[List[str]] = None

    class Config:
        allow_population_by_field_name = True


CredentialDefinitionsCreatedResult.update_forward_refs()
