import pydantic
import pytest
import logging

from aries_cloudcontroller.model.v10_presentation_exchange import (
    V10PresentationExchange,
)

LOGGER = logging.getLogger(__name__)

# From sample response in Swagger UI
valid_presentation = {
    "auto_present": "false",
    "connection_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "created_at": "2021-04-08 09:04:01Z",
    "error_msg": "Invalid structure",
    "initiator": "self",
    "presentation": {},
    "presentation_exchange_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "presentation_proposal_dict": {
        "presentation_proposal": {"attributes": [], "predicates": []}
    },
    "presentation_request": {"requested_attributes": {}, "requested_predicates": {}},
    "presentation_request_dict": {"request_presentations~attach": [{"data": {}}]},
    "role": "prover",
    "state": "verified",
    "thread_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "trace": "true",
    "updated_at": "2021-04-08 09:04:01Z",
    "verified": "true",
}

invalid_presentation = {
    "auto_present": "",  # should be bool
    "auto_verify": "",  # should be bool
    "connection_id": [],  # should be str
    "created_at": [],  # should be str
    "error_msg": [],  # should be str
    "initiator": "other",  # should be one of literal
    "presentation": "invalid",  # should be dict
    "presentation_exchange_id": [],  # should be str
    "presentation_proposal_dict": "",  # should be dict
    "presentation_request": "",  # should be dict
    "presentation_request_dict": "",  # should be dict
    "role": "other",  # should be one of literal
    "state": [],  # should be str
    "thread_id": [],  # should be str
    "trace": "",  # should be list
    "updated_at": [],  # should be str
    "verified": "other",  # should be one of literal
    "verified_msgs": "",  # should be list
}


def test_init_valid():
    # Should not throw validation errors
    V10PresentationExchange(**valid_presentation)


def test_invalid():
    for key, value in invalid_presentation.items():
        with pytest.raises(pydantic.error_wrappers.ValidationError):
            V10PresentationExchange(**{key: value})
