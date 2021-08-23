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

from aries_cloudcontroller.model.v10_credential_bound_offer_request import V10CredentialBoundOfferRequest
from aries_cloudcontroller.model.v10_credential_create import V10CredentialCreate
from aries_cloudcontroller.model.v10_credential_exchange import V10CredentialExchange
from aries_cloudcontroller.model.v10_credential_exchange_list_result import V10CredentialExchangeListResult
from aries_cloudcontroller.model.v10_credential_free_offer_request import V10CredentialFreeOfferRequest
from aries_cloudcontroller.model.v10_credential_issue_request import V10CredentialIssueRequest
from aries_cloudcontroller.model.v10_credential_problem_report_request import V10CredentialProblemReportRequest
from aries_cloudcontroller.model.v10_credential_proposal_request_mand import V10CredentialProposalRequestMand
from aries_cloudcontroller.model.v10_credential_proposal_request_opt import V10CredentialProposalRequestOpt
from aries_cloudcontroller.model.v10_credential_store_request import V10CredentialStoreRequest


class IssueCredentialV10Api(Consumer):
    @returns.json
    @json
    @post("/issue-credential/create")
    def create_credential(self, *, body: Body(type=V10CredentialCreate) = {}) -> V10CredentialExchange:
        """Send holder a credential, automating entire flow"""

    @returns.json
    @delete("/issue-credential/records/{cred_ex_id}")
    def delete_record(self, *, cred_ex_id: str) -> Dict:
        """Remove an existing credential exchange record"""

    @returns.json
    @get("/issue-credential/records/{cred_ex_id}")
    def get_record(self, *, cred_ex_id: str) -> V10CredentialExchange:
        """Fetch a single credential exchange record"""

    @returns.json
    @get("/issue-credential/records")
    def get_records(self, *, connection_id: Query = None, role: Query = None, state: Query = None, thread_id: Query = None) -> V10CredentialExchangeListResult:
        """Fetch all credential exchange records"""

    @returns.json
    @json
    @post("/issue-credential/records/{cred_ex_id}/issue")
    def issue_credential(self, *, cred_ex_id: str, body: Body(type=V10CredentialIssueRequest) = {}) -> V10CredentialExchange:
        """Send holder a credential"""

    @returns.json
    @json
    @post("/issue-credential/send")
    def issue_credential_automated(self, *, body: Body(type=V10CredentialProposalRequestMand) = {}) -> V10CredentialExchange:
        """Send holder a credential, automating entire flow"""

    @returns.json
    @json
    @post("/issue-credential/records/{cred_ex_id}/problem-report")
    def report_problem(self, *, cred_ex_id: str, body: Body(type=V10CredentialProblemReportRequest) = {}) -> Dict:
        """Send a problem report for credential exchange"""

    @returns.json
    @json
    @post("/issue-credential/records/{cred_ex_id}/send-offer")
    def send_offer(self, *, cred_ex_id: str, body: Body(type=V10CredentialBoundOfferRequest) = {}) -> V10CredentialExchange:
        """Send holder a credential offer in reference to a proposal with preview"""

    @returns.json
    @json
    @post("/issue-credential/send-offer")
    def send_offer_free(self, *, body: Body(type=V10CredentialFreeOfferRequest) = {}) -> V10CredentialExchange:
        """Send holder a credential offer, independent of any proposal"""

    @returns.json
    @json
    @post("/issue-credential/send-proposal")
    def send_proposal(self, *, body: Body(type=V10CredentialProposalRequestOpt) = {}) -> V10CredentialExchange:
        """Send issuer a credential proposal"""

    @returns.json
    @post("/issue-credential/records/{cred_ex_id}/send-request")
    def send_request(self, *, cred_ex_id: str) -> V10CredentialExchange:
        """Send issuer a credential request"""

    @returns.json
    @json
    @post("/issue-credential/records/{cred_ex_id}/store")
    def store_credential(self, *, cred_ex_id: str, body: Body(type=V10CredentialStoreRequest) = {}) -> V10CredentialExchange:
        """Store a received credential"""

