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

from aries_cloudcontroller.model.did_create import DIDCreate
from aries_cloudcontroller.model.did_endpoint import DIDEndpoint
from aries_cloudcontroller.model.did_endpoint_with_type import DIDEndpointWithType
from aries_cloudcontroller.model.did_list import DIDList
from aries_cloudcontroller.model.did_result import DIDResult


class WalletApi(Consumer):
    @returns.json
    @json
    @post("/wallet/did/create")
    def create_did(self, *, body: Body(type=DIDCreate) = {}) -> DIDResult:
        """Create a local DID"""

    @returns.json
    @get("/wallet/get-did-endpoint")
    def get_did_endpoint(self, *, did: Query) -> DIDEndpoint:
        """Query DID endpoint in wallet"""

    @returns.json
    @get("/wallet/did")
    def get_dids(
        self,
        *,
        did: Query = None,
        key_type: Query = None,
        method: Query = None,
        posture: Query = None,
        verkey: Query = None
    ) -> DIDList:
        """List wallet DIDs"""

    @returns.json
    @get("/wallet/did/public")
    def get_public_did(self) -> DIDResult:
        """Fetch the current public DID"""

    @returns.json
    @patch("/wallet/did/local/rotate-keypair")
    def rotate_keypair(self, *, did: Query) -> Dict:
        """Rotate keypair for a DID not posted to the ledger"""

    @returns.json
    @json
    @post("/wallet/set-did-endpoint")
    def set_did_endpoint(self, *, body: Body(type=DIDEndpointWithType) = {}) -> Dict:
        """Update endpoint in wallet and on ledger if posted to it"""

    @returns.json
    @post("/wallet/did/public")
    def set_public_did(self, *, did: Query) -> DIDResult:
        """Assign the current public DID"""
