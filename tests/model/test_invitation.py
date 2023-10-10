import logging

import pydantic
import pytest

from aries_cloudcontroller.models import InvitationMessage
from tests.util.compare_dicts import equal_dicts

LOGGER = logging.getLogger(__name__)

sample_invitation_message = {
    "@type": "https://didcomm.org/out-of-band/%VER/invitation",
    "@id": "<id used for context as pthid>",
    "label": "Faber College",
    "accept": ["didcomm/aip2;env=rfc587", "didcomm/aip2;env=rfc19"],
    "handshake_protocols": [
        "https://didcomm.org/didexchange/1.0",
        "https://didcomm.org/connections/1.0",
    ],
    "requests~attach": [
        {
            "@id": "request-0",
            "mime-type": "application/json",
            "data": {"json": {"example": "message"}},
        }
    ],
    "services": ["did:sov:LjgpST2rjsoxYegQDRm7EL"],
}

invalid_invitation_message = {
    "@id": ["unexpected", "list"],  # should be a string
    "@type": ["unexpected", "list"],  # should be a string
    "imageUrl": ["unexpected", "list"],  # should be a string
    "accept": "not a list or dict",  # should be a list
    "handshake_protocols": "not a list or dict",  # should be a list
    "requests~attach": "not a list or dict",  # should be a list
    "services": "not a list or dict",  # should be a list
}


def test_valid():
    model = InvitationMessage(**sample_invitation_message)
    assert equal_dicts(sample_invitation_message, model.model_dump(by_alias=True))


def test_invalid():
    for key, value in invalid_invitation_message.items():
        with pytest.raises(pydantic.ValidationError):
            InvitationMessage(**{key: value})
