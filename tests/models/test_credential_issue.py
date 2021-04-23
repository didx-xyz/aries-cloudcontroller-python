import pytest
import json
import logging

from aries_cloudcontroller.models.credential_issue import CredentialIssue

LOGGER = logging.getLogger(__name__)

pytest.cred_keys = [
    "@type",
    "@id",
    "goal_code",
    "replacement_id",
    "comment",
    "formats",
    "requests~attach",
]

# From sample in https://github.com/hyperledger/aries-rfcs/tree/master/features/0453-issue-credential-v2
pytest.valid_cred_req = json.dumps(
    {
        "@type": "https://didcomm.org/issue-credential/%VER/request-credential",
        "@id": "987654321",
        "goal_code": "123456789",
        "replacement_id": "<issuer unique id>",
        "comment": "An awesome comment",
        "formats": [
            {
                "attach_id": "<attach@id value>",
                "format": "<format-and-version>",
            }
        ],
        "requests~attach": [
            {
                "@id": "<attachment identifier>",
                "mime-type": "application/json",
                "data": {"base64": "<bytes for base64>"},
            },
        ],
    }
)

pytest.invalid_cred_req = json.dumps(
    {
        "@id": "987654321",
        "goal_code": "123456789",
        "replacement_id": "<issuer unique id>",
        "comment": "An awesome comment",
        "formats": [
            {
                "attach_id": "<attach@id value>",
                "format": "<format-and-version>",
            }
        ],
        "requests~attach": [
            {
                "@id": "<attachment identifier>",
                "mime-type": "application/json",
                "data": {"base64": "<bytes for base64>"},
            },
        ],
    }
)

pytest.not_json = 123456

pytest.invalid_cred_req = json.dumps({"abc": "1234"})

pytest.multi_formats = json.dumps(
    {
        "@type": "https://didcomm.org/issue-credential/%VER/request-credential",
        "@id": "987654321",
        "goal_code": "123456789",
        "replacement_id": "<issuer unique id>",
        "comment": "An awesome comment",
        "formats": [
            {
                "attach_id": "<attach@id value>",
                "format": "<format-and-version>",
            },
            {
                "attach_id": "<attach@id value>",
                "format": "<format-and-version>",
            },
        ],
        "requests~attach": [
            {
                "@id": "<attachment identifier>",
                "mime-type": "application/json",
                "data": {"base64": "<bytes for base64>"},
            },
        ],
    }
)

pytest.multi_attach = json.dumps(
    {
        "@type": "https://didcomm.org/issue-credential/%VER/request-credential",
        "@id": "987654321",
        "goal_code": "123456789",
        "replacement_id": "<issuer unique id>",
        "comment": "An awesome comment",
        "formats": [],
        "requests~attach": [
            {
                "@id": "<attachment identifier>",
                "mime-type": "application/json",
                "data": {"base64": "<bytes for base64>"},
            },
            {
                "@id": "<attachment identifier>",
                "mime-type": "application/json",
                "data": {"base64": "<bytes for base64>"},
            },
        ],
    }
)


def test_init_valid():
    cred_req = CredentialIssue(pytest.valid_cred_req)
    assert cred_req.json_data == json.loads(pytest.valid_cred_req)


def test_init_invalid():
    with pytest.raises(AssertionError, match="Missing key"):
        CredentialIssue(pytest.invalid_cred_req)


def test_init_not_json(caplog):
    error_msg = "the JSON object must be str, bytes or bytearray, not int"
    with pytest.raises(TypeError, match=error_msg):
        CredentialIssue(pytest.not_json)
    assert "Failed to load credentials request JSON" in caplog.text


# check for each possibly missing key whether the correct error is raised
@pytest.mark.parametrize("key", pytest.cred_keys)
def test_validate_credential_issue_json(key):
    creds = pytest.valid_cred_req
    cred_obj = CredentialIssue(creds)
    with pytest.raises(AssertionError, match=f"Missing key {key}"):
        del cred_obj.json_data[key]
        cred_obj.validate_credential_issue_json(json.dumps(cred_obj.json_data))


def test_get_formats():
    expected = [
        {
            "attach_id": "<attach@id value>",
            "format": "<format-and-version>",
        }
    ]
    formats = CredentialIssue(pytest.valid_cred_req).get_formats()
    assert formats == expected


def test_get_attachments():
    expected = [
        {
            "@id": "<attachment identifier>",
            "mime-type": "application/json",
            "data": {"base64": "<bytes for base64>"},
        },
    ]
    attachments = CredentialIssue(pytest.valid_cred_req).get_attachments()
    assert attachments == expected


def test_multi_format():
    expected = [
        {
            "attach_id": "<attach@id value>",
            "format": "<format-and-version>",
        },
        {
            "attach_id": "<attach@id value>",
            "format": "<format-and-version>",
        },
    ]
    formats = CredentialIssue(pytest.multi_formats).get_formats()
    assert formats == expected


def test_get_attachments():
    expected = [
        {
            "@id": "<attachment identifier>",
            "mime-type": "application/json",
            "data": {"base64": "<bytes for base64>"},
        },
        {
            "@id": "<attachment identifier>",
            "mime-type": "application/json",
            "data": {"base64": "<bytes for base64>"},
        },
    ]
    attachments = CredentialIssue(pytest.multi_attach).get_attachments()
    assert attachments == expected


def test_get_type():
    expected = "https://didcomm.org/issue-credential/%VER/request-credential"
    connection_id = CredentialIssue(pytest.valid_cred_req).get_type()
    assert connection_id == expected


def test_get_id():
    expected = "987654321"
    id = CredentialIssue(pytest.valid_cred_req).get_id()
    assert id == expected


def test_get_goal_code():
    expected = "123456789"
    goal_code = CredentialIssue(pytest.valid_cred_req).get_goal_code()
    assert goal_code == expected


def test_get_comment():
    expected = "An awesome comment"
    comment = CredentialIssue(pytest.valid_cred_req).get_comments()
    assert comment == expected
