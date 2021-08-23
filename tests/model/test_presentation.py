import pytest
import json
import logging

from aries_cloudcontroller.model.v10_presentation_exchange import (
    V10PresentationExchange,
)

LOGGER = logging.getLogger(__name__)

presentation_keys = [
    "auto_present",
    "connection_id",
    "created_at",
    "error_msg",
    "initiator",
    "presentation",
    "presentation_exchange_id",
    "presentation_proposal_dict",
    "presentation_request",
    "presentation_request_dict",
    "role",
    "state",
    "thread_id",
    "trace",
    "updated_at",
    "verified",
]

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
    "presentation_request": {},
    "presentation_request_dict": {"request_presentations~attach": {"data": {}}},
    "role": "prover",
    "state": "verified",
    "thread_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "trace": "true",
    "updated_at": "2021-04-08 09:04:01Z",
    "verified": "true",
}


unverified_presentation = {
    "auto_present": "false",
    "connection_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "created_at": "2021-04-08 09:04:01Z",
    "error_msg": "Invalid structure",
    "initiator": "self",
    "presentation": {},
    "presentation_exchange_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "presentation_proposal_dict": {},
    "presentation_request": {},
    "presentation_request_dict": {},
    "role": "prover",
    "state": "verified",
    "thread_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "trace": "true",
    "updated_at": "2021-04-08 09:04:01Z",
    "verified": "false",
}


invalid_presentation = {"abc": "1234"}

not_json = 123456

self_attested_attrs_json = {
    "auto_present": "false",
    "connection_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "created_at": "2021-04-08 09:04:01Z",
    "error_msg": "Invalid structure",
    "initiator": "self",
    "presentation": {
        "requested_proof": {
            "self_attested_attrs": {
                "item1": {"raw": "sth"},
                "item2": {"raw": "sth"},
                "item3": {"raw": "sth"},
            },
        },
    },
    "presentation_exchange_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "presentation_proposal_dict": {},
    "presentation_request": {},
    "presentation_request_dict": {},
    "role": "prover",
    "state": "verified",
    "thread_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "trace": "true",
    "updated_at": "2021-04-08 09:04:01Z",
    "verified": "true",
}


revealed_attrs_json = {
    "auto_present": "false",
    "connection_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "created_at": "2021-04-08 09:04:01Z",
    "error_msg": "Invalid structure",
    "initiator": "self",
    "presentation": {
        "requested_proof": {
            "revealed_attrs": {
                "item1": {"raw": "sth"},
                "item2": {"raw": "sth"},
                "item3": {"raw": "sth"},
            },
        },
    },
    "presentation_exchange_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "presentation_proposal_dict": {},
    "presentation_request": {},
    "presentation_request_dict": {},
    "role": "prover",
    "state": "verified",
    "thread_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "trace": "true",
    "updated_at": "2021-04-08 09:04:01Z",
    "verified": "true",
}

unrevealed_attrs_json = {
    "auto_present": "false",
    "connection_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "created_at": "2021-04-08 09:04:01Z",
    "error_msg": "Invalid structure",
    "initiator": "self",
    "presentation": {
        "requested_proof": {
            "unrevealed_attrs": {
                "item1": {"raw": "sth"},
                "item2": {"raw": "sth"},
                "item3": {"raw": "sth"},
            },
        },
    },
    "presentation_exchange_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "presentation_proposal_dict": {},
    "presentation_request": {},
    "presentation_request_dict": {},
    "role": "prover",
    "state": "verified",
    "thread_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "trace": "true",
    "updated_at": "2021-04-08 09:04:01Z",
    "verified": "true",
}


predicates_attrs_json = {
    "auto_present": "false",
    "connection_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "created_at": "2021-04-08 09:04:01Z",
    "error_msg": "Invalid structure",
    "initiator": "self",
    "presentation": {
        "requested_proof": {
            "predicates": {
                "item1": {"raw": "sth"},
                "item2": {"raw": "sth"},
                "item3": {"raw": "sth"},
            },
        },
    },
    "presentation_exchange_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "presentation_proposal_dict": {},
    "presentation_request": {},
    "presentation_request_dict": {},
    "role": "prover",
    "state": "verified",
    "thread_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "trace": "true",
    "updated_at": "2021-04-08 09:04:01Z",
    "verified": "true",
}

identifiers_json = {
    "auto_present": "false",
    "connection_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "created_at": "2021-04-08 09:04:01Z",
    "error_msg": "Invalid structure",
    "initiator": "self",
    "presentation": {
        "identifiers": [
            {
                "rev_reg_id": "123456789",
                "cred_def_id": "123456789",
                "schema_id": "123456789",
            },
            {
                "rev_reg_id": "987654321",
                "cred_def_id": "987654321",
                "schema_id": "987654321",
            },
        ]
    },
    "presentation_exchange_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "presentation_proposal_dict": {},
    "presentation_request": {},
    "presentation_request_dict": {},
    "role": "prover",
    "state": "verified",
    "thread_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "trace": "true",
    "updated_at": "2021-04-08 09:04:01Z",
    "verified": "true",
}


def test_init_valid():
    pres = V10PresentationExchange(**valid_presentation)
    assert pres.json_data == json.loads(valid_presentation)


def test_init_invalid():
    with pytest.raises(AssertionError, match="Missing key"):
        V10PresentationExchange(invalid_presentation)
