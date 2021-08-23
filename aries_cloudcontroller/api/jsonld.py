from uplink import (
    Consumer,
    get,
    Path,
    Query,
    Body,
    post,
    get,
    patch,
    put,
    delete,
    Header,
    returns,
    json,
)

from typing import Dict, List  # noqa: F401

from aries_cloudcontroller.model.sign_request import SignRequest
from aries_cloudcontroller.model.sign_response import SignResponse
from aries_cloudcontroller.model.verify_request import VerifyRequest
from aries_cloudcontroller.model.verify_response import VerifyResponse


class JsonldApi(Consumer):
    @returns.json
    @json
    @post("/jsonld/sign")
    def sign(self, *, body: Body(type=SignRequest) = {}) -> SignResponse:
        """Sign a JSON-LD structure and return it"""

    @returns.json
    @json
    @post("/jsonld/verify")
    def verify(self, *, body: Body(type=VerifyRequest) = {}) -> VerifyResponse:
        """Verify a JSON-LD structure."""
