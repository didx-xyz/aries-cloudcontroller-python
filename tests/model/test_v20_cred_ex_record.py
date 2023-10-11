import logging

import pydantic
import pytest

from aries_cloudcontroller.models import V20CredExRecord
from tests.util.compare_dicts import equal_dicts

LOGGER = logging.getLogger(__name__)

sample_cred_ex_record = {
    "auto_issue": True,
    "auto_offer": True,
    "auto_remove": False,
    "by_format": {
        "cred_issue": {"cred_issue_attach_id": "sample_id"},
        "cred_offer": {"cred_offer_attach_id": "sample_id"},
        "cred_proposal": {"cred_proposal_attach_id": "sample_id"},
        "cred_request": {"cred_request_attach_id": "sample_id"},
    },
    "connection_id": "connection_id_example",
    "created_at": "2023-05-24 00:00:00Z",
    "cred_ex_id": "1234567890",
    "cred_issue": {
        "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/issue-credential/2.0/issue-credential",
        "credentials~attach": [
            {
                "@id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "mime-type": "application/json",
                "data": {"base64": "eyJuYW1lIjogIkpvZSIsICJhZ2UiOiAzMH0="},
            }
        ],
        "formats": [
            {
                "attach_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "format": "hlindy/cred-abstract@v2.0",
            }
        ],
    },
    "cred_offer": {
        "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/issue-credential/2.0/offer-credential",
        "@id": "7890359123456",
        "offers~attach": [
            {
                "@id": "attach-id-1",
                "mime-type": "application/json",
                "data": {
                    "base64": "eyJhbGciOiJFZERTQSJ9hTYXQiOjE0NzYzMjM4MzgsImF1ZCI6Ind3dz=="
                },
            }
        ],
        "formats": [
            {
                "attach_id": "abc85f64-5717-4562-b3fc-2c963f66afa6",
                "format": "hlindy/cred-abstract@v2.0",
            }
        ],
    },
    "cred_preview": {
        "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/issue-credential/2.0/credential-preview",
        "attributes": [{"name": "name", "value": "John Doe"}],
    },
    "cred_proposal": {
        "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/issue-credential/2.0/propose-credential",
        "@id": "7890359123456",
        "filters~attach": [
            {
                "@id": "filters-id-1",
                "mime-type": "application/json",
                "data": {
                    "base64": "abchbGciOiJFZERTQSJ9hTYXQiOjE0NzYzMjM4MzgsImF1ZCI6Ind3dz=="
                },
            }
        ],
        "formats": [
            {
                "attach_id": "def85f64-5717-4562-b3fc-2c963f66afa6",
                "format": "hlindy/cred-abstract@v2.0",
            }
        ],
    },
    "cred_request": {
        "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/issue-credential/2.0/request-credential",
        "@id": "7890359123457",
        "requests~attach": [
            {
                "@id": "requests-id-1",
                "mime-type": "application/json",
                "data": {
                    "base64": "defgbGciOiJFZERTQSJ9hTYXQiOjE0NzYzMjM4MzgsImF1ZCI6Ind3dz=="
                },
            }
        ],
        "formats": [
            {
                "attach_id": "ghi85f64-5717-4562-b3fc-2c963f66afa6",
                "format": "hlindy/cred-abstract@v2.0",
            }
        ],
    },
    "error_msg": "no error",
    "initiator": "self",
    "parent_thread_id": "parent_thread_id_example",
    "role": "issuer",
    "state": "credential-issued",
    "thread_id": "1234567890",
    "trace": False,
    "updated_at": "2023-05-24 00:01:00Z",
}

invalid_cred_ex_record = {
    "auto_issue": "",  # should be bool
    "auto_offer": "",  # should be bool
    "auto_remove": "",  # should be bool
    "by_format": "_",  # should be dict
    "connection_id": [],  # should be str
    "created_at": [],  # should be str
    "cred_ex_id": [],  # should be str
    "cred_issue": "",  # should be dict
    "cred_offer": "",  # should be dict
    "cred_preview": "",  # should be dict
    "cred_proposal": "",  # should be dict
    "cred_request": "",  # should be dict
    "error_msg": [],  # should be str
    "initiator": "other",  # should be one of literal
    "parent_thread_id": [],  # should be str
    "role": "other",  # should be one of literal
    "state": [],  # should be one of literal
    "thread_id": [],  # should be str
    "trace": "",  # should be bool
    "updated_at": [],  # should be str
}


def test_valid():
    model = V20CredExRecord(**sample_cred_ex_record)
    assert equal_dicts(sample_cred_ex_record, model.model_dump(by_alias=True))


def test_invalid():
    for key, value in invalid_cred_ex_record.items():
        with pytest.raises(pydantic.ValidationError):
            V20CredExRecord(**{key: value})
