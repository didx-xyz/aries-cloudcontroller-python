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
from aries_cloudcontroller.model.didx_request import DIDXRequest


class DidExchangeApi(Consumer):
    @returns.json
    @post("/didexchange/{conn_id}/accept-invitation")
    def accept_invitation(self, *, conn_id: str, my_endpoint: Query = None, my_label: Query = None) -> ConnRecord:
        """Accept a stored connection invitation"""

    @returns.json
    @post("/didexchange/{conn_id}/accept-request")
    def accept_request(self, *, conn_id: str, mediation_id: Query = None, my_endpoint: Query = None) -> ConnRecord:
        """Accept a stored connection request"""

    @returns.json
    @post("/didexchange/create-request")
    def create_request(self, *, their_public_did: Query, mediation_id: Query = None, my_endpoint: Query = None, my_label: Query = None, use_public_did: Query = None) -> ConnRecord:
        """Create and send a request against public DID's implicit invitation"""

    @returns.json
    @json
    @post("/didexchange/receive-request")
    def receive_request(self, *, alias: Query = None, auto_accept: Query = None, mediation_id: Query = None, my_endpoint: Query = None, body: Body(type=DIDXRequest) = {}) -> ConnRecord:
        """Receive request against public DID's implicit invitation"""

