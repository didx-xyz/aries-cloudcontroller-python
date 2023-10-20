import logging

import pydantic
import pytest

from aries_cloudcontroller.models import V20PresExRecord
from tests.util.compare_dicts import equal_dicts

LOGGER = logging.getLogger(__name__)

sample_pres_ex_record = {
    "auto_present": True,
    "auto_verify": True,
    "by_format": {"pres": {"attach_id": "sample_id"}},
    "connection_id": "connection_id_example",
    "created_at": "2023-05-24 00:00:00Z",
    "error_msg": "no error",
    "initiator": "self",
    "pres": {
        "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/present-proof/2.0/presentation",
        "@id": "5678876542345",
        "presentations~attach": [
            {
                "@id": "6942f0a4-af51-4f62-a0ca-001bdc030cb4",
                "mime-type": "application/json",
                "data": {"base64": "eyJuYW1lIjogIkpvZSIsICJhZ2UiOiAzMH0="},
            }
        ],
        "formats": [
            {
                "attach_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "format": "hlindy/pres-abstract@v2.0",
            }
        ],
    },
    "pres_ex_id": "1234567890",
    "pres_proposal": {
        "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/present-proof/2.0/propose-presentation",
        "@id": "7890359123456",
        "proposals~attach": [
            {
                "@id": "proposal-attach-id-1",
                "mime-type": "application/json",
                "data": {
                    "base64": "abchbGciOiJFZERTQSJ9hTYXQiOjE0NzYzMjM4MzgsImF1ZCI6Ind3dz=="
                },
            }
        ],
        "formats": [
            {
                "attach_id": "def85f64-5717-4562-b3fc-2c963f66afa6",
                "format": "hlindy/pres-abstract@v2.0",
            }
        ],
    },
    "pres_request": {
        "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/present-proof/2.0/request-presentation",
        "@id": "7890359123457",
        "request_presentations~attach": [
            {
                "@id": "request-attach-id-1",
                "mime-type": "application/json",
                "data": {
                    "base64": "defgbGciOiJFZERTQSJ9hTYXQiOjE0NzYzMjM4MzgsImF1ZCI6Ind3dz=="
                },
            }
        ],
        "formats": [
            {
                "attach_id": "ghi85f64-5717-4562-b3fc-2c963f66afa6",
                "format": "hlindy/pres-abstract@v2.0",
            }
        ],
    },
    "role": "prover",
    "state": "presentation-sent",
    "thread_id": "1234567890",
    "trace": False,
    "updated_at": "2023-05-24 00:01:00Z",
    "verified": "true",
    "verified_msgs": ["msg1", "msg2"],
}


invalid_pres_ex_record = {
    "auto_present": "",  # should be bool
    "auto_verify": "",  # should be bool
    "by_format": "_",  # should be dict
    "connection_id": [],  # should be str
    "created_at": [],  # should be str
    "error_msg": [],  # should be str
    "initiator": "other",  # should be one of literal
    "pres": "",  # should be dict
    "pres_ex_id": [],  # should be str
    "pres_proposal": "",  # should be dict
    "pres_request": "",  # should be dict
    "role": "other",  # should be one of literal
    "state": [],  # should be one of literal
    "thread_id": [],  # should be str
    "trace": "",  # should be bool
    "updated_at": [],  # should be str
    "verified": "",  # should be bool
    "verified_msgs": "",  # should be list
}


def test_valid():
    model = V20PresExRecord(**sample_pres_ex_record)
    assert equal_dicts(sample_pres_ex_record, model.model_dump(by_alias=True))


def test_invalid():
    for key, value in invalid_pres_ex_record.items():
        with pytest.raises(pydantic.ValidationError):
            V20PresExRecord(**{key: value})
