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

from aries_cloudcontroller.model.ping_request import PingRequest
from aries_cloudcontroller.model.ping_request_response import PingRequestResponse


class TrustpingApi(Consumer):
    @returns.json
    @json
    @post("/connections/{conn_id}/send-ping")
    def send_ping(
        self, *, conn_id: str, body: Body(type=PingRequest) = {}
    ) -> PingRequestResponse:
        """Send a trust ping to a connection"""
