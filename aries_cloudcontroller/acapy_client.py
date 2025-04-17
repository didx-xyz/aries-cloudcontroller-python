from contextlib import AbstractAsyncContextManager
from typing import Optional

from aries_cloudcontroller.api import (
    ActionMenuApi,
    AnonCredsCredentialDefinitionsApi,
    AnonCredsRevocationApi,
    AnonCredsSchemasApi,
    AnonCredsWalletUpgradeApi,
    BasicmessageApi,
    ConnectionApi,
    CredentialDefinitionApi,
    CredentialsApi,
    DefaultApi,
    DidExchangeApi,
    DidRotateApi,
    DiscoverFeaturesApi,
    DiscoverFeaturesV20Api,
    EndorseTransactionApi,
    IntroductionApi,
    IssueCredentialV10Api,
    IssueCredentialV20Api,
    JsonldApi,
    LedgerApi,
    MediationApi,
    MultitenancyApi,
    OutOfBandApi,
    PresentProofV10Api,
    PresentProofV20Api,
    ResolverApi,
    RevocationApi,
    SchemaApi,
    ServerApi,
    SettingsApi,
    TrustpingApi,
    WalletApi,
)
from aries_cloudcontroller.api_client import ApiClient
from aries_cloudcontroller.configuration import Configuration


class AcaPyClient(AbstractAsyncContextManager):
    action_menu: ActionMenuApi
    anoncreds_credential_definitions: AnonCredsCredentialDefinitionsApi
    anoncreds_revocation: AnonCredsRevocationApi
    anoncreds_schemas: AnonCredsSchemasApi
    anoncreds_wallet_upgrade: AnonCredsWalletUpgradeApi
    basicmessage: BasicmessageApi
    connection: ConnectionApi
    credential_definition: CredentialDefinitionApi
    credentials: CredentialsApi
    default: DefaultApi
    did_exchange: DidExchangeApi
    did_rotate: DidRotateApi
    discover_features: DiscoverFeaturesApi
    discover_features_v2_0: DiscoverFeaturesV20Api
    endorse_transaction: EndorseTransactionApi
    introduction: IntroductionApi
    issue_credential_v1_0: IssueCredentialV10Api
    issue_credential_v2_0: IssueCredentialV20Api
    jsonld: JsonldApi
    ledger: LedgerApi
    mediation: MediationApi
    multitenancy: MultitenancyApi
    out_of_band: OutOfBandApi
    present_proof_v1_0: PresentProofV10Api
    present_proof_v2_0: PresentProofV20Api
    resolver: ResolverApi
    revocation: RevocationApi
    schema: SchemaApi
    server: ServerApi
    settings: SettingsApi
    trustping: TrustpingApi
    wallet: WalletApi

    def __init__(
        self,
        base_url: str,
        *,
        api_key: Optional[str] = None,
        tenant_jwt: Optional[str] = None,
        admin_insecure: Optional[bool] = False,
    ):
        if not api_key and not admin_insecure:
            raise Exception(
                "api_key property is missing. Use admin_insecure=True if you want"
                " to use the controller without authentication."
            )

        self.api_key = api_key
        self.tenant_jwt = tenant_jwt

        # We will configure an ApiClient instance and pass it to our API modules
        self.configuration = Configuration(host=base_url)
        self.api_client = ApiClient(self.configuration)

        # ApiClient init can only take one header, so configure api_key and tenant_jwt separately
        if api_key:
            self.api_client.default_headers["x-api-key"] = api_key
        if tenant_jwt:
            self.api_client.default_headers["Authorization"] = f"Bearer {tenant_jwt}"

        # Initialize the API modules
        self.action_menu = ActionMenuApi(self.api_client)
        self.anoncreds_credential_definitions = AnonCredsCredentialDefinitionsApi(
            self.api_client
        )
        self.anoncreds_revocation = AnonCredsRevocationApi(self.api_client)
        self.anoncreds_schemas = AnonCredsSchemasApi(self.api_client)
        self.anoncreds_wallet_upgrade = AnonCredsWalletUpgradeApi(self.api_client)
        self.basicmessage = BasicmessageApi(self.api_client)
        self.connection = ConnectionApi(self.api_client)
        self.credential_definition = CredentialDefinitionApi(self.api_client)
        self.credentials = CredentialsApi(self.api_client)
        self.default = DefaultApi(self.api_client)
        self.did_exchange = DidExchangeApi(self.api_client)
        self.did_rotate = DidRotateApi(self.api_client)
        self.discover_features = DiscoverFeaturesApi(self.api_client)
        self.discover_features_v2_0 = DiscoverFeaturesV20Api(self.api_client)
        self.endorse_transaction = EndorseTransactionApi(self.api_client)
        self.introduction = IntroductionApi(self.api_client)
        self.issue_credential_v1_0 = IssueCredentialV10Api(self.api_client)
        self.issue_credential_v2_0 = IssueCredentialV20Api(self.api_client)
        self.jsonld = JsonldApi(self.api_client)
        self.ledger = LedgerApi(self.api_client)
        self.mediation = MediationApi(self.api_client)
        self.multitenancy = MultitenancyApi(self.api_client)
        self.out_of_band = OutOfBandApi(self.api_client)
        self.present_proof_v1_0 = PresentProofV10Api(self.api_client)
        self.present_proof_v2_0 = PresentProofV20Api(self.api_client)
        self.resolver = ResolverApi(self.api_client)
        self.revocation = RevocationApi(self.api_client)
        self.schema = SchemaApi(self.api_client)
        self.server = ServerApi(self.api_client)
        self.settings = SettingsApi(self.api_client)
        self.trustping = TrustpingApi(self.api_client)
        self.wallet = WalletApi(self.api_client)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

    async def close(self):
        await self.api_client.close()
