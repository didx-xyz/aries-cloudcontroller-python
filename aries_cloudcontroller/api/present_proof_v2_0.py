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
from aries_cloudcontroller.model.v20_pres_create_request_request import (
    V20PresCreateRequestRequest,
)
from aries_cloudcontroller.model.v20_pres_ex_record import V20PresExRecord
from aries_cloudcontroller.model.v20_pres_ex_record_list import V20PresExRecordList
from aries_cloudcontroller.model.v20_pres_problem_report_request import (
    V20PresProblemReportRequest,
)
from aries_cloudcontroller.model.v20_pres_proposal_request import V20PresProposalRequest
from aries_cloudcontroller.model.v20_pres_send_request_request import (
    V20PresSendRequestRequest,
)
from aries_cloudcontroller.model.v20_pres_spec_by_format_request import (
    V20PresSpecByFormatRequest,
)


class PresentProofV20Api(Consumer):
    @returns.json
    @json
    @post("/present-proof-2.0/create-request")
    def create_proof_request(
        self, *, body: Body(type=V20PresCreateRequestRequest) = {}
    ) -> V20PresExRecord:
        """Creates a presentation request not bound to any proposal or connection"""

    @returns.json
    @delete("/present-proof-2.0/records/{pres_ex_id}")
    def delete_record(self, *, pres_ex_id: str) -> Dict:
        """Remove an existing presentation exchange record"""

    @returns.json
    @get("/present-proof-2.0/records/{pres_ex_id}/credentials")
    def get_matching_credentials(
        self,
        *,
        pres_ex_id: str,
        count: Query = None,
        extra_query: Query = None,
        referent: Query = None,
        start: Query = None
    ) -> List[IndyCredPrecis]:
        """Fetch credentials from wallet for presentation request"""

    @returns.json
    @get("/present-proof-2.0/records/{pres_ex_id}")
    def get_record(self, *, pres_ex_id: str) -> V20PresExRecord:
        """Fetch a single presentation exchange record"""

    @returns.json
    @get("/present-proof-2.0/records")
    def get_records(
        self,
        *,
        connection_id: Query = None,
        role: Query = None,
        state: Query = None,
        thread_id: Query = None
    ) -> V20PresExRecordList:
        """Fetch all present-proof exchange records"""

    @returns.json
    @json
    @post("/present-proof-2.0/records/{pres_ex_id}/problem-report")
    def report_problem(
        self, *, pres_ex_id: str, body: Body(type=V20PresProblemReportRequest) = {}
    ) -> Dict:
        """Send a problem report for presentation exchange"""

    @returns.json
    @json
    @post("/present-proof-2.0/records/{pres_ex_id}/send-presentation")
    def send_presentation(
        self, *, pres_ex_id: str, body: Body(type=V20PresSpecByFormatRequest) = {}
    ) -> V20PresExRecord:
        """Sends a proof presentation"""

    @returns.json
    @json
    @post("/present-proof-2.0/send-proposal")
    def send_proposal(
        self, *, body: Body(type=V20PresProposalRequest) = {}
    ) -> V20PresExRecord:
        """Sends a presentation proposal"""

    @returns.json
    @json
    @post("/present-proof-2.0/records/{pres_ex_id}/send-request")
    def send_request(
        self, *, pres_ex_id: str, body: Body(type=AdminAPIMessageTracing) = {}
    ) -> V20PresExRecord:
        """Sends a presentation request in reference to a proposal"""

    @returns.json
    @json
    @post("/present-proof-2.0/send-request")
    def send_request_free(
        self, *, body: Body(type=V20PresSendRequestRequest) = {}
    ) -> V20PresExRecord:
        """Sends a free presentation request not bound to any proposal"""

    @returns.json
    @post("/present-proof-2.0/records/{pres_ex_id}/verify-presentation")
    def verify_presentation(self, *, pres_ex_id: str) -> V20PresExRecord:
        """Verify a received presentation"""
