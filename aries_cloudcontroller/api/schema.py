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

from aries_cloudcontroller.model.schema_get_result import SchemaGetResult
from aries_cloudcontroller.model.schema_send_request import SchemaSendRequest
from aries_cloudcontroller.model.schemas_created_result import SchemasCreatedResult
from aries_cloudcontroller.model.txn_or_schema_send_result import TxnOrSchemaSendResult


class SchemaApi(Consumer):
    @returns.json
    @get("/schemas/created")
    def get_created_schemas(
        self,
        *,
        schema_id: Query = None,
        schema_issuer_did: Query = None,
        schema_name: Query = None,
        schema_version: Query = None
    ) -> SchemasCreatedResult:
        """Search for matching schema that agent originated"""

    @returns.json
    @get("/schemas/{schema_id}")
    def get_schema(self, *, schema_id: str) -> SchemaGetResult:
        """Gets a schema from the ledger"""

    @returns.json
    @json
    @post("/schemas")
    def publish_schema(
        self,
        *,
        conn_id: Query = None,
        create_transaction_for_endorser: Query = None,
        body: Body(type=SchemaSendRequest) = {}
    ) -> TxnOrSchemaSendResult:
        """Sends a schema to the ledger"""
