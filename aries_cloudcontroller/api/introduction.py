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


class IntroductionApi(Consumer):
    @returns.json
    @post("/connections/{conn_id}/start-introduction")
    def start_introduction(
        self, *, conn_id: str, target_connection_id: Query, message: Query = None
    ) -> Dict:
        """Start an introduction between two connections"""
