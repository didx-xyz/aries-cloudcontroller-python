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

from aries_cloudcontroller.model.v20_cred_bound_offer_request import V20CredBoundOfferRequest
from aries_cloudcontroller.model.v20_cred_ex_record import V20CredExRecord
from aries_cloudcontroller.model.v20_cred_ex_record_detail import V20CredExRecordDetail
from aries_cloudcontroller.model.v20_cred_ex_record_list_result import V20CredExRecordListResult
from aries_cloudcontroller.model.v20_cred_issue_problem_report_request import V20CredIssueProblemReportRequest
from aries_cloudcontroller.model.v20_cred_issue_request import V20CredIssueRequest
from aries_cloudcontroller.model.v20_cred_offer_request import V20CredOfferRequest
from aries_cloudcontroller.model.v20_cred_request_free import V20CredRequestFree
from aries_cloudcontroller.model.v20_cred_request_request import V20CredRequestRequest
from aries_cloudcontroller.model.v20_cred_send_request import V20CredSendRequest
from aries_cloudcontroller.model.v20_cred_store_request import V20CredStoreRequest
from aries_cloudcontroller.model.v20_issue_cred_schema_core import V20IssueCredSchemaCore


class IssueCredentialV20Api(Consumer):
    @returns.json
    @json
    @post("/issue-credential-2.0/create")
    def create_credential(self, *, body: Body(type=V20IssueCredSchemaCore) = {}) -> V20CredExRecord:
        """Create credential from attribute values"""

    @returns.json
    @delete("/issue-credential-2.0/records/{cred_ex_id}")
    def delete_record(self, *, cred_ex_id: str) -> Dict:
        """Remove an existing credential exchange record"""

    @returns.json
    @get("/issue-credential-2.0/records/{cred_ex_id}")
    def get_record(self, *, cred_ex_id: str) -> V20CredExRecordDetail:
        """Fetch a single credential exchange record"""

    @returns.json
    @get("/issue-credential-2.0/records")
    def get_records(self, *, connection_id: Query = None, role: Query = None, state: Query = None, thread_id: Query = None) -> V20CredExRecordListResult:
        """Fetch all credential exchange records"""

    @returns.json
    @json
    @post("/issue-credential-2.0/records/{cred_ex_id}/issue")
    def issue_credential(self, *, cred_ex_id: str, body: Body(type=V20CredIssueRequest) = {}) -> V20CredExRecordDetail:
        """Send holder a credential"""

    @returns.json
    @json
    @post("/issue-credential-2.0/send")
    def issue_credential_automated(self, *, body: Body(type=V20CredSendRequest) = {}) -> V20CredExRecord:
        """Send holder a credential, automating entire flow"""

    @returns.json
    @json
    @post("/issue-credential-2.0/records/{cred_ex_id}/problem-report")
    def report_problem(self, *, cred_ex_id: str, body: Body(type=V20CredIssueProblemReportRequest) = {}) -> Dict:
        """Send a problem report for credential exchange"""

    @returns.json
    @json
    @post("/issue-credential-2.0/records/{cred_ex_id}/send-offer")
    def send_offer(self, *, cred_ex_id: str, body: Body(type=V20CredBoundOfferRequest) = {}) -> V20CredExRecord:
        """Send holder a credential offer in reference to a proposal with preview"""

    @returns.json
    @json
    @post("/issue-credential-2.0/send-offer")
    def send_offer_free(self, *, body: Body(type=V20CredOfferRequest) = {}) -> V20CredExRecord:
        """Send holder a credential offer, independent of any proposal"""

    @returns.json
    @json
    @post("/issue-credential-2.0/send-proposal")
    def send_proposal(self, *, body: Body(type=V20IssueCredSchemaCore) = {}) -> V20CredExRecord:
        """Send issuer a credential proposal"""

    @returns.json
    @json
    @post("/issue-credential-2.0/records/{cred_ex_id}/send-request")
    def send_request(self, *, cred_ex_id: str, body: Body(type=V20CredRequestRequest) = {}) -> V20CredExRecord:
        """Send issuer a credential request"""

    @returns.json
    @json
    @post("/issue-credential-2.0/send-request")
    def send_request_free(self, *, body: Body(type=V20CredRequestFree) = {}) -> V20CredExRecord:
        """Send issuer a credential request not bound to an existing thread. Indy credentials cannot start at a request"""

    @returns.json
    @json
    @post("/issue-credential-2.0/records/{cred_ex_id}/store")
    def store_credential(self, *, cred_ex_id: str, body: Body(type=V20CredStoreRequest) = {}) -> V20CredExRecordDetail:
        """Store a received credential"""

