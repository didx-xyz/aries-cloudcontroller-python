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

from aries_cloudcontroller.model.admin_config import AdminConfig
from aries_cloudcontroller.model.admin_modules import AdminModules
from aries_cloudcontroller.model.admin_status import AdminStatus
from aries_cloudcontroller.model.admin_status_liveliness import AdminStatusLiveliness
from aries_cloudcontroller.model.admin_status_readiness import AdminStatusReadiness
from aries_cloudcontroller.model.query_result import QueryResult


class ServerApi(Consumer):
    @returns.json
    @get("/status/live")
    def check_liveliness(self) -> AdminStatusLiveliness:
        """Liveliness check"""

    @returns.json
    @get("/status/config")
    def get_config(self) -> AdminConfig:
        """Fetch the server configuration"""

    @returns.json
    @get("/features")
    def get_features(self, *, query: Query = None) -> QueryResult:
        """Query supported features"""

    @returns.json
    @get("/plugins")
    def get_plugins(self) -> AdminModules:
        """Fetch the list of loaded plugins"""

    @returns.json
    @get("/status/ready")
    def get_ready_state(self) -> AdminStatusReadiness:
        """Readiness check"""

    @returns.json
    @get("/status")
    def get_status(self) -> AdminStatus:
        """Fetch the server status"""

    @returns.json
    @post("/status/reset")
    def reset_statistics(self) -> Dict:
        """Reset statistics"""

    @returns.json
    @get("/shutdown")
    def shutdown_server(self) -> Dict:
        """Shut down server"""
