import logging

import pydantic
import pytest

from aries_cloudcontroller.models import CredentialOffer
from tests.util.compare_dicts import equal_dicts

LOGGER = logging.getLogger(__name__)

sample_credential_offer = {
    "@id": "123456789abcdefghi",
    "@type": "https://didcomm.org/issue-credential/1.0/offer-credential",
    "comment": "This is a credential offer",
    "offers~attach": [
        {
            "@id": "attach-id-1",
            "mime-type": "application/json",
            "data": {
                "base64": "eyJhbGciOiJFZERTQSJ9hTYXQiOjE0NzYzMjM4MzgsImF1ZCI6Ind3dz=="
            },
        },
        {
            "@id": "attach-id-2",
            "mime-type": "application/json",
            "data": {
                "base64": "eyJhbGciOiJFZERTQSJ9hTYXQiOjE0NzYzMjM4MzgsImF1ZCI6Ind3dz=="
            },
        },
    ],
    "credential_preview": {
        "@type": "https://didcomm.org/issue-credential/1.0/credential-preview",
        "attributes": [{"name": "attribute_name", "value": "attribute_value"}],
    },
}


invalid_credential_offer = {
    "@id": ["unexpected", "list"],  # should be a string
    "@type": ["unexpected", "list"],  # should be a string
    "comment": ["unexpected", "list"],  # should be a string
    "offers~attach": "not a list or dict",  # should be a list
    "credential_preview": "not a list or dict",  # should be a list
}


def test_valid():
    model = CredentialOffer(**sample_credential_offer)
    assert equal_dicts(sample_credential_offer, model.model_dump(by_alias=True))


def test_invalid():
    for key, value in invalid_credential_offer.items():
        with pytest.raises(pydantic.ValidationError):
            CredentialOffer(offersattach=[], **{key: value})
