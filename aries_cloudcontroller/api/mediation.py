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

from aries_cloudcontroller.model.admin_mediation_deny import AdminMediationDeny
from aries_cloudcontroller.model.keylist import Keylist
from aries_cloudcontroller.model.keylist_query import KeylistQuery
from aries_cloudcontroller.model.keylist_query_filter_request import KeylistQueryFilterRequest
from aries_cloudcontroller.model.keylist_update import KeylistUpdate
from aries_cloudcontroller.model.keylist_update_request import KeylistUpdateRequest
from aries_cloudcontroller.model.mediation_create_request import MediationCreateRequest
from aries_cloudcontroller.model.mediation_deny import MediationDeny
from aries_cloudcontroller.model.mediation_grant import MediationGrant
from aries_cloudcontroller.model.mediation_list import MediationList
from aries_cloudcontroller.model.mediation_record import MediationRecord


class MediationApi(Consumer):
    @returns.json
    @delete("/mediation/default-mediator")
    def clear_default_mediator(self) -> MediationRecord:
        """Clear default mediator"""

    @returns.json
    @delete("/mediation/requests/{mediation_id}")
    def delete_record(self, *, mediation_id: str) -> MediationRecord:
        """Delete mediation request by ID"""

    @returns.json
    @json
    @post("/mediation/requests/{mediation_id}/deny")
    def deny_mediation_request(self, *, mediation_id: str, body: Body(type=AdminMediationDeny) = {}) -> MediationDeny:
        """Deny a stored mediation request"""

    @returns.json
    @get("/mediation/default-mediator")
    def get_default_mediator(self) -> MediationRecord:
        """Get default mediator"""

    @returns.json
    @get("/mediation/requests/{mediation_id}")
    def get_record(self, *, mediation_id: str) -> MediationRecord:
        """Retrieve mediation request record"""

    @returns.json
    @get("/mediation/requests")
    def get_records(self, *, conn_id: Query = None, mediator_terms: Query = None, recipient_terms: Query = None, state: Query = None) -> MediationList:
        """Query mediation requests, returns list of all mediation records"""

    @returns.json
    @post("/mediation/requests/{mediation_id}/grant")
    def grant_mediation_request(self, *, mediation_id: str) -> MediationGrant:
        """Grant received mediation"""

    @returns.json
    @json
    @post("/mediation/request/{conn_id}")
    def request_mediation(self, *, conn_id: str, body: Body(type=MediationCreateRequest) = {}) -> MediationRecord:
        """Request mediation from connection"""

    @returns.json
    @get("/mediation/keylists")
    def retrieve_keylists(self, *, conn_id: Query = None, role: Query = 'server') -> Keylist:
        """Retrieve keylists by connection or role"""

    @returns.json
    @json
    @post("/mediation/keylists/{mediation_id}/send-keylist-query")
    def send_keylist_query(self, *, mediation_id: str, paginate_limit: Query = -1, paginate_offset: Query = 0, body: Body(type=KeylistQueryFilterRequest) = {}) -> KeylistQuery:
        """Send keylist query to mediator"""

    @returns.json
    @json
    @post("/mediation/keylists/{mediation_id}/send-keylist-update")
    def send_keylist_update(self, *, mediation_id: str, body: Body(type=KeylistUpdateRequest) = {}) -> KeylistUpdate:
        """Send keylist update to mediator"""

    @returns.json
    @put("/mediation/{mediation_id}/default-mediator")
    def set_default_mediator(self, *, mediation_id: str) -> MediationRecord:
        """Set default mediator"""

