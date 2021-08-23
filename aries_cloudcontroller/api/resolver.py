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

from aries_cloudcontroller.model.resolution_result import ResolutionResult


class ResolverApi(Consumer):
    @returns.json
    @get("/resolver/resolve/{did}")
    def get_did(self, *, did: str) -> ResolutionResult:
        """Retrieve doc for requested did"""

