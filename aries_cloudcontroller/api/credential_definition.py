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

from aries_cloudcontroller.model.credential_definition_get_result import (
    CredentialDefinitionGetResult,
)
from aries_cloudcontroller.model.credential_definition_send_request import (
    CredentialDefinitionSendRequest,
)
from aries_cloudcontroller.model.credential_definitions_created_result import (
    CredentialDefinitionsCreatedResult,
)
from aries_cloudcontroller.model.txn_or_credential_definition_send_result import (
    TxnOrCredentialDefinitionSendResult,
)


class CredentialDefinitionApi(Consumer):
    @returns.json
    @get("/credential-definitions/created")
    def get_created_cred_defs(
        self,
        *,
        cred_def_id: Query = None,
        issuer_did: Query = None,
        schema_id: Query = None,
        schema_issuer_did: Query = None,
        schema_name: Query = None,
        schema_version: Query = None
    ) -> CredentialDefinitionsCreatedResult:
        """Search for matching credential definitions that agent originated"""

    @returns.json
    @get("/credential-definitions/{cred_def_id}")
    def get_cred_def(self, *, cred_def_id: str) -> CredentialDefinitionGetResult:
        """Gets a credential definition from the ledger"""

    @returns.json
    @json
    @post("/credential-definitions")
    def publish_cred_def(
        self,
        *,
        conn_id: Query = None,
        create_transaction_for_endorser: Query = None,
        body: Body(type=CredentialDefinitionSendRequest) = {}
    ) -> TxnOrCredentialDefinitionSendResult:
        """Sends a credential definition to the ledger"""
