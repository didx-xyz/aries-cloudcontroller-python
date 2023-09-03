from typing import Any, Dict, List, Optional, Union  # noqa: F401

from uplink import (
    Body,
    Consumer,
    Header,
    Path,
    Query,
    delete,
    get,
    json,
    patch,
    post,
    put,
    returns,
)

from aries_cloudcontroller.model.resolution_result import ResolutionResult
from aries_cloudcontroller.uplink_util import bool_query


class ResolverApi(Consumer):
    async def get_did(self, *, did: str) -> ResolutionResult:
        """Retrieve doc for requested did"""
        return await self.__get_did(
            did=did,
        )

    @returns.json
    @get("/resolver/resolve/{did}")
    def __get_did(self, *, did: str) -> ResolutionResult:
        """Internal uplink method for get_did"""
