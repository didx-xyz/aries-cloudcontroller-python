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

from aries_cloudcontroller.model.conn_record import ConnRecord
from aries_cloudcontroller.model.invitation_create_request import (
    InvitationCreateRequest,
)
from aries_cloudcontroller.model.invitation_message import InvitationMessage
from aries_cloudcontroller.model.invitation_record import InvitationRecord


class OutOfBandApi(Consumer):
    @returns.json
    @json
    @post("/out-of-band/create-invitation")
    def create_invitation(
        self,
        *,
        auto_accept: Query = None,
        multi_use: Query = None,
        body: Body(type=InvitationCreateRequest) = {}
    ) -> InvitationRecord:
        """Create a new connection invitation"""

    @returns.json
    @json
    @post("/out-of-band/receive-invitation")
    def receive_invitation(
        self,
        *,
        alias: Query = None,
        auto_accept: Query = None,
        mediation_id: Query = None,
        use_existing_connection: Query = None,
        body: Body(type=InvitationMessage) = {}
    ) -> ConnRecord:
        """Receive a new connection invitation"""
