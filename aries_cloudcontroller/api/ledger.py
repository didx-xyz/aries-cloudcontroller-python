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

from aries_cloudcontroller.model.get_did_endpoint_response import GetDIDEndpointResponse
from aries_cloudcontroller.model.get_did_verkey_response import GetDIDVerkeyResponse
from aries_cloudcontroller.model.get_nym_role_response import GetNymRoleResponse
from aries_cloudcontroller.model.register_ledger_nym_response import (
    RegisterLedgerNymResponse,
)
from aries_cloudcontroller.model.taa_accept import TAAAccept
from aries_cloudcontroller.model.taa_result import TAAResult


class LedgerApi(Consumer):
    @returns.json
    @json
    @post("/ledger/taa/accept")
    def accept_taa(self, *, body: Body(type=TAAAccept) = {}) -> Dict:
        """Accept the transaction author agreement"""

    @returns.json
    @get("/ledger/taa")
    def fetch_taa(self) -> TAAResult:
        """Fetch the current transaction author agreement, if any"""

    @returns.json
    @get("/ledger/did-endpoint")
    def get_did_endpoint(
        self, *, did: Query, endpoint_type: Query = None
    ) -> GetDIDEndpointResponse:
        """Get the endpoint for a DID from the ledger."""

    @returns.json
    @get("/ledger/get-nym-role")
    def get_did_nym_role(self, *, did: Query) -> GetNymRoleResponse:
        """Get the role from the NYM registration of a public DID."""

    @returns.json
    @get("/ledger/did-verkey")
    def get_did_verkey(self, *, did: Query) -> GetDIDVerkeyResponse:
        """Get the verkey for a DID from the ledger."""

    @returns.json
    @post("/ledger/register-nym")
    def register_nym(
        self, *, did: Query, verkey: Query, alias: Query = None, role: Query = None
    ) -> RegisterLedgerNymResponse:
        """Send a NYM registration to the ledger."""

    @returns.json
    @patch("/ledger/rotate-public-did-keypair")
    def rotate_public_did_keypair(self) -> Dict:
        """Rotate key pair for public DID."""
