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

from aries_cloudcontroller.model.send_message import SendMessage


class BasicmessageApi(Consumer):
    @returns.json
    @json
    @post("/connections/{conn_id}/send-message")
    def send_message(self, *, conn_id: str, body: Body(type=SendMessage) = {}) -> Dict:
        """Send a basic message to a connection"""
