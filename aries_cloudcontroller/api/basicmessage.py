from typing import Any, Dict, List, Optional, Union  # noqa: F401

from uplink import (
    Body,
    Consumer,
    Header,
    Path,
    Query,
    delete,
    get,
    json,
    patch,
    post,
    put,
    returns,
)

from aries_cloudcontroller.model.send_message import SendMessage
from aries_cloudcontroller.uplink_util import bool_query


class BasicmessageApi(Consumer):
    async def send_message(
        self, *, conn_id: str, body: Optional[SendMessage] = None
    ) -> Dict[str, Any]:
        """Send a basic message to a connection"""
        if not body:
            body = SendMessage()
        return await self.__send_message(
            conn_id=conn_id,
            body=body,
        )

    @returns.json
    @json
    @post("/connections/{conn_id}/send-message")
    def __send_message(
        self, *, conn_id: str, body: Body(type=SendMessage) = {}
    ) -> Dict[str, Any]:
        """Internal uplink method for send_message"""
