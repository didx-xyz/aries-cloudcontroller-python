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

from aries_cloudcontroller.model.action_menu_fetch_result import ActionMenuFetchResult
from aries_cloudcontroller.model.perform_request import PerformRequest
from aries_cloudcontroller.model.send_menu import SendMenu


class ActionMenuApi(Consumer):
    @returns.json
    @post("/action-menu/{conn_id}/close")
    def close_active_menu(self, *, conn_id: str) -> Dict:
        """Close the active menu associated with a connection"""

    @returns.json
    @post("/action-menu/{conn_id}/fetch")
    def fetch_active_menu(self, *, conn_id: str) -> ActionMenuFetchResult:
        """Fetch the active menu"""

    @returns.json
    @json
    @post("/action-menu/{conn_id}/perform")
    def perform_action(self, *, conn_id: str, body: Body(type=PerformRequest) = {}) -> Dict:
        """Perform an action associated with the active menu"""

    @returns.json
    @post("/action-menu/{conn_id}/request")
    def request_active_menu(self, *, conn_id: str) -> Dict:
        """Request the active menu"""

    @returns.json
    @json
    @post("/action-menu/{conn_id}/send-menu")
    def send_menu(self, *, conn_id: str, body: Body(type=SendMenu) = {}) -> Dict:
        """Send an action menu to a connection"""

