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

from typing import Dict, List, Optional  # noqa: F401

from aries_cloudcontroller.model.ping_request import PingRequest
from aries_cloudcontroller.model.ping_request_response import PingRequestResponse


class TrustpingApi(Consumer):
    async def send_ping(
        self, *, conn_id: str, body: Optional[PingRequest] = None
    ) -> PingRequestResponse:
        """Send a trust ping to a connection"""
        return await self.__send_ping(
            conn_id=conn_id,
            body=body,
        )

    @returns.json
    @json
    @post("/connections/{conn_id}/send-ping")
    def __send_ping(
        self, *, conn_id: str, body: Body(type=PingRequest) = {}
    ) -> PingRequestResponse:
        """Internal uplink method for send_ping"""
