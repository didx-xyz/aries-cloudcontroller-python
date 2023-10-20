import logging

import pydantic
import pytest

from aries_cloudcontroller.models import DID
from tests.util.compare_dicts import equal_dicts

LOGGER = logging.getLogger(__name__)

sample_did = {
    "key_type": "ed25519",
    "method": "sov",
    "posture": "public",
}

invalid_did_key_type = {
    "key_type": "invalidKeyType",  # invalid key type
    "method": "sov",
    "posture": "public",
}

invalid_did_method = {
    "key_type": "ed25519",
    "method": "invalidMethod",  # invalid method
    "posture": "public",
}

invalid_did_posture = {
    "key_type": "ed25519",
    "method": "sov",
    "posture": "invalidPosture",  # invalid posture
}

sample_did_with_ed25519_verkey = {
    "key_type": "ed25519",  # ED25519 key type
    "verkey": "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijk",  # 44 base58 characters
}

sample_did_with_bbs_verkey = {
    "key_type": "bls12381g2",  # BBS+ key type
    "verkey": "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz123456789ABCD"
    "EFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz123456789ABCDEFG",  # 132 characters
}

invalid_did_with_verkey = {
    "verkey": "invalidVerkey",  # invalid verkey format
}


def test_valid_did():
    model = DID(**sample_did)
    assert equal_dicts(sample_did, model.model_dump(by_alias=True))


def test_invalid_key_type():
    with pytest.raises(pydantic.ValidationError):
        DID(**invalid_did_key_type)


def test_invalid_method():
    with pytest.raises(pydantic.ValidationError):
        DID(**invalid_did_method)


def test_invalid_posture():
    with pytest.raises(pydantic.ValidationError):
        DID(**invalid_did_posture)


def test_valid_did_with_ed25519_verkey():
    model = DID(**sample_did_with_ed25519_verkey)
    assert equal_dicts(sample_did_with_ed25519_verkey, model.model_dump(by_alias=True))


def test_valid_did_with_bbs_verkey():
    model = DID(**sample_did_with_bbs_verkey)
    assert equal_dicts(sample_did_with_bbs_verkey, model.model_dump(by_alias=True))


def test_invalid_verkey():
    with pytest.raises(pydantic.ValidationError):
        DID(**invalid_did_with_verkey)
