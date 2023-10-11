from typing import Optional

from aries_cloudcontroller.api import (
    ActionMenuApi,
    BasicmessageApi,
    ConnectionApi,
    CredentialDefinitionApi,
    CredentialsApi,
    DefaultApi,
    DidExchangeApi,
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


class AcaPyClient(ApiClient):
    action_menu: ActionMenuApi
    basicmessage: BasicmessageApi
    connection: ConnectionApi
    credential_definition: CredentialDefinitionApi
    credentials: CredentialsApi
    default: DefaultApi
    did_exchange: DidExchangeApi
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

        # Initialize the parent ApiClient
        super().__init__()

        # Custom setup from base_url, api_key, and tenant_jwt
        self.configuration.host = base_url
        if api_key:
            self.default_headers["x-api-key"] = api_key
        if tenant_jwt:
            self.default_headers["Authorization"] = f"Bearer {tenant_jwt}"

        # Initialize the API modules
        self.action_menu = ActionMenuApi(self)
        self.basicmessage = BasicmessageApi(self)
        self.connection = ConnectionApi(self)
        self.credential_definition = CredentialDefinitionApi(self)
        self.credentials = CredentialsApi(self)
        self.default = DefaultApi(self)
        self.did_exchange = DidExchangeApi(self)
        self.discover_features = DiscoverFeaturesApi(self)
        self.discover_features_v2_0 = DiscoverFeaturesV20Api(self)
        self.endorse_transaction = EndorseTransactionApi(self)
        self.introduction = IntroductionApi(self)
        self.issue_credential_v1_0 = IssueCredentialV10Api(self)
        self.issue_credential_v2_0 = IssueCredentialV20Api(self)
        self.jsonld = JsonldApi(self)
        self.ledger = LedgerApi(self)
        self.mediation = MediationApi(self)
        self.multitenancy = MultitenancyApi(self)
        self.out_of_band = OutOfBandApi(self)
        self.present_proof_v1_0 = PresentProofV10Api(self)
        self.present_proof_v2_0 = PresentProofV20Api(self)
        self.resolver = ResolverApi(self)
        self.revocation = RevocationApi(self)
        self.schema = SchemaApi(self)
        self.server = ServerApi(self)
        self.settings = SettingsApi(self)
        self.trustping = TrustpingApi(self)
        self.wallet = WalletApi(self)
