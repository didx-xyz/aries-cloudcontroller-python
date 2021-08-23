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
from aries_cloudcontroller.model.connection_list import ConnectionList
from aries_cloudcontroller.model.connection_metadata import ConnectionMetadata
from aries_cloudcontroller.model.connection_metadata_set_request import ConnectionMetadataSetRequest
from aries_cloudcontroller.model.connection_static_request import ConnectionStaticRequest
from aries_cloudcontroller.model.connection_static_result import ConnectionStaticResult
from aries_cloudcontroller.model.create_invitation_request import CreateInvitationRequest
from aries_cloudcontroller.model.endpoints_result import EndpointsResult
from aries_cloudcontroller.model.invitation_result import InvitationResult
from aries_cloudcontroller.model.receive_invitation_request import ReceiveInvitationRequest


class ConnectionApi(Consumer):
    @returns.json
    @post("/connections/{conn_id}/accept-invitation")
    def accept_invitation(self, *, conn_id: str, mediation_id: Query = None, my_endpoint: Query = None, my_label: Query = None) -> ConnRecord:
        """Accept a stored connection invitation"""

    @returns.json
    @post("/connections/{conn_id}/accept-request")
    def accept_request(self, *, conn_id: str, my_endpoint: Query = None) -> ConnRecord:
        """Accept a stored connection request"""

    @returns.json
    @json
    @post("/connections/create-invitation")
    def create_invitation(self, *, alias: Query = None, auto_accept: Query = None, multi_use: Query = None, public: Query = None, body: Body(type=CreateInvitationRequest) = {}) -> InvitationResult:
        """Create a new connection invitation"""

    @returns.json
    @json
    @post("/connections/create-static")
    def create_static_connection(self, *, body: Body(type=ConnectionStaticRequest) = {}) -> ConnectionStaticResult:
        """Create a new static connection"""

    @returns.json
    @delete("/connections/{conn_id}")
    def delete_connection(self, *, conn_id: str) -> Dict:
        """Remove an existing connection record"""

    @returns.json
    @post("/connections/{conn_id}/establish-inbound/{ref_id}")
    def establish_inbound(self, *, conn_id: str, ref_id: str) -> Dict:
        """Assign another connection as the inbound connection"""

    @returns.json
    @get("/connections/{conn_id}")
    def get_connection(self, *, conn_id: str) -> ConnRecord:
        """Fetch a single connection record"""

    @returns.json
    @get("/connections/{conn_id}/endpoints")
    def get_connection_endpoint(self, *, conn_id: str) -> EndpointsResult:
        """Fetch connection remote endpoint"""

    @returns.json
    @get("/connections")
    def get_connections(self, *, alias: Query = None, connection_protocol: Query = None, invitation_key: Query = None, my_did: Query = None, state: Query = None, their_did: Query = None, their_role: Query = None) -> ConnectionList:
        """Query agent-to-agent connections"""

    @returns.json
    @get("/connections/{conn_id}/metadata")
    def get_metadata(self, *, conn_id: str, key: Query = None) -> ConnectionMetadata:
        """Fetch connection metadata"""

    @returns.json
    @json
    @post("/connections/receive-invitation")
    def receive_invitation(self, *, alias: Query = None, auto_accept: Query = None, mediation_id: Query = None, body: Body(type=ReceiveInvitationRequest) = {}) -> ConnRecord:
        """Receive a new connection invitation"""

    @returns.json
    @json
    @post("/connections/{conn_id}/metadata")
    def set_metadata(self, *, conn_id: str, body: Body(type=ConnectionMetadataSetRequest) = {}) -> ConnectionMetadata:
        """Set connection metadata"""

