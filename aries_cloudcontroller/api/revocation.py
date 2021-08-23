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

from aries_cloudcontroller.model.clear_pending_revocations_request import (
    ClearPendingRevocationsRequest,
)
from aries_cloudcontroller.model.cred_rev_record_result import CredRevRecordResult
from aries_cloudcontroller.model.publish_revocations import PublishRevocations
from aries_cloudcontroller.model.rev_reg_create_request import RevRegCreateRequest
from aries_cloudcontroller.model.rev_reg_issued_result import RevRegIssuedResult
from aries_cloudcontroller.model.rev_reg_result import RevRegResult
from aries_cloudcontroller.model.rev_reg_update_tails_file_uri import (
    RevRegUpdateTailsFileUri,
)
from aries_cloudcontroller.model.rev_regs_created import RevRegsCreated
from aries_cloudcontroller.model.revoke_request import RevokeRequest
from aries_cloudcontroller.model.txn_or_publish_revocations_result import (
    TxnOrPublishRevocationsResult,
)
from aries_cloudcontroller.model.txn_or_rev_reg_result import TxnOrRevRegResult


class RevocationApi(Consumer):
    @returns.json
    @json
    @post("/revocation/clear-pending-revocations")
    def clear_pending_revocations(
        self, *, body: Body(type=ClearPendingRevocationsRequest) = {}
    ) -> PublishRevocations:
        """Clear pending revocations"""

    @returns.json
    @json
    @post("/revocation/create-registry")
    def create_registry(
        self, *, body: Body(type=RevRegCreateRequest) = {}
    ) -> RevRegResult:
        """Creates a new revocation registry"""

    @get("/revocation/registry/{rev_reg_id}/tails-file")
    def download_tails_file(self, *, rev_reg_id: str) -> bytes:
        """Download tails file"""

    @returns.json
    @get("/revocation/active-registry/{cred_def_id}")
    def get_active_registry_for_cred_def(self, *, cred_def_id: str) -> RevRegResult:
        """Get current active revocation registry by credential definition id"""

    @returns.json
    @get("/revocation/registries/created")
    def get_created_registries(
        self, *, cred_def_id: Query = None, state: Query = None
    ) -> RevRegsCreated:
        """Search for matching revocation registries that current agent created"""

    @returns.json
    @get("/revocation/registry/{rev_reg_id}")
    def get_registry(self, *, rev_reg_id: str) -> RevRegResult:
        """Get revocation registry by revocation registry id"""

    @returns.json
    @get("/revocation/registry/{rev_reg_id}/issued")
    def get_registry_issued_credentials_count(
        self, *, rev_reg_id: str
    ) -> RevRegIssuedResult:
        """Get number of credentials issued against revocation registry"""

    @returns.json
    @get("/revocation/credential-record")
    def get_revocation_status(
        self,
        *,
        cred_ex_id: Query = None,
        cred_rev_id: Query = None,
        rev_reg_id: Query = None
    ) -> CredRevRecordResult:
        """Get credential revocation status"""

    @returns.json
    @post("/revocation/registry/{rev_reg_id}/definition")
    def publish_rev_reg_def(
        self,
        *,
        rev_reg_id: str,
        conn_id: Query = None,
        create_transaction_for_endorser: Query = None
    ) -> TxnOrRevRegResult:
        """Send revocation registry definition to ledger"""

    @returns.json
    @post("/revocation/registry/{rev_reg_id}/entry")
    def publish_rev_reg_entry(
        self,
        *,
        rev_reg_id: str,
        conn_id: Query = None,
        create_transaction_for_endorser: Query = None
    ) -> RevRegResult:
        """Send revocation registry entry to ledger"""

    @returns.json
    @json
    @post("/revocation/publish-revocations")
    def publish_revocations(
        self,
        *,
        conn_id: Query = None,
        create_transaction_for_endorser: Query = None,
        body: Body(type=PublishRevocations) = {}
    ) -> TxnOrPublishRevocationsResult:
        """Publish pending revocations to ledger"""

    @returns.json
    @json
    @post("/revocation/revoke")
    def revoke_credential(self, *, body: Body(type=RevokeRequest) = {}) -> Dict:
        """Revoke an issued credential"""

    @returns.json
    @patch("/revocation/registry/{rev_reg_id}/set-state")
    def set_registry_state(self, *, rev_reg_id: str, state: Query) -> RevRegResult:
        """Set revocation registry state manually"""

    @returns.json
    @json
    @patch("/revocation/registry/{rev_reg_id}")
    def update_registry(
        self, *, rev_reg_id: str, body: Body(type=RevRegUpdateTailsFileUri) = {}
    ) -> RevRegResult:
        """Update revocation registry with new public URI to its tails file"""

    @returns.json
    @put("/revocation/registry/{rev_reg_id}/tails-file")
    def upload_tails_file(self, *, rev_reg_id: str) -> Dict:
        """Upload local tails file to server"""
