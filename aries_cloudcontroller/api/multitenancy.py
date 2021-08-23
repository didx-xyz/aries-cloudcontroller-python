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

from aries_cloudcontroller.model.create_wallet_request import CreateWalletRequest
from aries_cloudcontroller.model.create_wallet_response import CreateWalletResponse
from aries_cloudcontroller.model.create_wallet_token_request import (
    CreateWalletTokenRequest,
)
from aries_cloudcontroller.model.create_wallet_token_response import (
    CreateWalletTokenResponse,
)
from aries_cloudcontroller.model.remove_wallet_request import RemoveWalletRequest
from aries_cloudcontroller.model.update_wallet_request import UpdateWalletRequest
from aries_cloudcontroller.model.wallet_list import WalletList
from aries_cloudcontroller.model.wallet_record import WalletRecord


class MultitenancyApi(Consumer):
    @returns.json
    @json
    @post("/multitenancy/wallet")
    def create_wallet(
        self, *, body: Body(type=CreateWalletRequest) = {}
    ) -> CreateWalletResponse:
        """Create a subwallet"""

    @returns.json
    @json
    @post("/multitenancy/wallet/{wallet_id}/remove")
    def delete_wallet(
        self, *, wallet_id: str, body: Body(type=RemoveWalletRequest) = {}
    ) -> Dict:
        """Remove a subwallet"""

    @returns.json
    @json
    @post("/multitenancy/wallet/{wallet_id}/token")
    def get_auth_token(
        self, *, wallet_id: str, body: Body(type=CreateWalletTokenRequest) = {}
    ) -> CreateWalletTokenResponse:
        """Get auth token for a subwallet"""

    @returns.json
    @get("/multitenancy/wallet/{wallet_id}")
    def get_wallet(self, *, wallet_id: str) -> WalletRecord:
        """Get a single subwallet"""

    @returns.json
    @get("/multitenancy/wallets")
    def get_wallets(self, *, wallet_name: Query = None) -> WalletList:
        """Query subwallets"""

    @returns.json
    @json
    @put("/multitenancy/wallet/{wallet_id}")
    def update_wallet(
        self, *, wallet_id: str, body: Body(type=UpdateWalletRequest) = {}
    ) -> WalletRecord:
        """Update a subwallet"""
