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

from aries_cloudcontroller.model.admin_api_message_tracing import AdminAPIMessageTracing
from aries_cloudcontroller.model.indy_cred_precis import IndyCredPrecis
from aries_cloudcontroller.model.indy_pres_spec import IndyPresSpec
from aries_cloudcontroller.model.v10_presentation_create_request_request import V10PresentationCreateRequestRequest
from aries_cloudcontroller.model.v10_presentation_exchange import V10PresentationExchange
from aries_cloudcontroller.model.v10_presentation_exchange_list import V10PresentationExchangeList
from aries_cloudcontroller.model.v10_presentation_problem_report_request import V10PresentationProblemReportRequest
from aries_cloudcontroller.model.v10_presentation_proposal_request import V10PresentationProposalRequest
from aries_cloudcontroller.model.v10_presentation_send_request_request import V10PresentationSendRequestRequest


class PresentProofV10Api(Consumer):
    @returns.json
    @json
    @post("/present-proof/create-request")
    def create_proof_request(self, *, body: Body(type=V10PresentationCreateRequestRequest) = {}) -> V10PresentationExchange:
        """Creates a presentation request not bound to any proposal or connection"""

    @returns.json
    @delete("/present-proof/records/{pres_ex_id}")
    def delete_record(self, *, pres_ex_id: str) -> Dict:
        """Remove an existing presentation exchange record"""

    @returns.json
    @get("/present-proof/records/{pres_ex_id}/credentials")
    def get_matching_credentials(self, *, pres_ex_id: str, count: Query = None, extra_query: Query = None, referent: Query = None, start: Query = None) -> List[IndyCredPrecis]:
        """Fetch credentials for a presentation request from wallet"""

    @returns.json
    @get("/present-proof/records/{pres_ex_id}")
    def get_record(self, *, pres_ex_id: str) -> V10PresentationExchange:
        """Fetch a single presentation exchange record"""

    @returns.json
    @get("/present-proof/records")
    def get_records(self, *, connection_id: Query = None, role: Query = None, state: Query = None, thread_id: Query = None) -> V10PresentationExchangeList:
        """Fetch all present-proof exchange records"""

    @returns.json
    @json
    @post("/present-proof/records/{pres_ex_id}/problem-report")
    def report_problem(self, *, pres_ex_id: str, body: Body(type=V10PresentationProblemReportRequest) = {}) -> Dict:
        """Send a problem report for presentation exchange"""

    @returns.json
    @json
    @post("/present-proof/records/{pres_ex_id}/send-presentation")
    def send_presentation(self, *, pres_ex_id: str, body: Body(type=IndyPresSpec) = {}) -> V10PresentationExchange:
        """Sends a proof presentation"""

    @returns.json
    @json
    @post("/present-proof/send-proposal")
    def send_proposal(self, *, body: Body(type=V10PresentationProposalRequest) = {}) -> V10PresentationExchange:
        """Sends a presentation proposal"""

    @returns.json
    @json
    @post("/present-proof/records/{pres_ex_id}/send-request")
    def send_request(self, *, pres_ex_id: str, body: Body(type=AdminAPIMessageTracing) = {}) -> V10PresentationExchange:
        """Sends a presentation request in reference to a proposal"""

    @returns.json
    @json
    @post("/present-proof/send-request")
    def send_request_free(self, *, body: Body(type=V10PresentationSendRequestRequest) = {}) -> V10PresentationExchange:
        """Sends a free presentation request not bound to any proposal"""

    @returns.json
    @post("/present-proof/records/{pres_ex_id}/verify-presentation")
    def verify_presentation(self, *, pres_ex_id: str) -> V10PresentationExchange:
        """Verify a received presentation"""

