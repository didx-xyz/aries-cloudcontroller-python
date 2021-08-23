# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.claim_format import ClaimFormat
from aries_cloudcontroller.model.input_descriptors import InputDescriptors
from aries_cloudcontroller.model.submission_requirements import SubmissionRequirements


class PresentationDefinition(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PresentationDefinition - a model defined in OpenAPI
        format: The format of this PresentationDefinition [Optional].
        id: Unique Resource Identifier [Optional].
        input_descriptors: The input_descriptors of this PresentationDefinition [Optional].
        name: Human-friendly name that describes what the presentation definition pertains to [Optional].
        purpose: Describes the purpose for which the Presentation Definition&#39;s inputs are being requested [Optional].
        submission_requirements: The submission_requirements of this PresentationDefinition [Optional].
    """

    format: Optional[ClaimFormat] = None
    id: Optional[str] = None
    input_descriptors: Optional[List[InputDescriptors]] = None
    name: Optional[str] = None
    purpose: Optional[str] = None
    submission_requirements: Optional[List[SubmissionRequirements]] = None

    def __init__(
        self,
        *,
        format: Optional[ClaimFormat] = None,
        id: Optional[str] = None,
        input_descriptors: Optional[List[InputDescriptors]] = None,
        name: Optional[str] = None,
        purpose: Optional[str] = None,
        submission_requirements: Optional[List[SubmissionRequirements]] = None,
        **kwargs,
    ):
        super().__init__(
            format=format,
            id=id,
            input_descriptors=input_descriptors,
            name=name,
            purpose=purpose,
            submission_requirements=submission_requirements,
            **kwargs,
        )

    @validator("id")
    def id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"
        if not re.match(pattern, value):
            raise ValueError(f"Value of id does not match regex pattern ('{pattern}')")
        return value


PresentationDefinition.update_forward_refs()
