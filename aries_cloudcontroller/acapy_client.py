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


class AcaPyClient:
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

        # We will configure an ApiClient instance and pass it to our API modules
        api_client = ApiClient()

        # Custom setup from base_url, api_key, and tenant_jwt
        api_client.configuration.host = base_url
        if api_key:
            api_client.default_headers["x-api-key"] = api_key
        if tenant_jwt:
            api_client.default_headers["Authorization"] = f"Bearer {tenant_jwt}"

        # Initialize the API modules
        self.action_menu = ActionMenuApi(api_client)
        self.basicmessage = BasicmessageApi(api_client)
        self.connection = ConnectionApi(api_client)
        self.credential_definition = CredentialDefinitionApi(api_client)
        self.credentials = CredentialsApi(api_client)
        self.default = DefaultApi(api_client)
        self.did_exchange = DidExchangeApi(api_client)
        self.discover_features = DiscoverFeaturesApi(api_client)
        self.discover_features_v2_0 = DiscoverFeaturesV20Api(api_client)
        self.endorse_transaction = EndorseTransactionApi(api_client)
        self.introduction = IntroductionApi(api_client)
        self.issue_credential_v1_0 = IssueCredentialV10Api(api_client)
        self.issue_credential_v2_0 = IssueCredentialV20Api(api_client)
        self.jsonld = JsonldApi(api_client)
        self.ledger = LedgerApi(api_client)
        self.mediation = MediationApi(api_client)
        self.multitenancy = MultitenancyApi(api_client)
        self.out_of_band = OutOfBandApi(api_client)
        self.present_proof_v1_0 = PresentProofV10Api(api_client)
        self.present_proof_v2_0 = PresentProofV20Api(api_client)
        self.resolver = ResolverApi(api_client)
        self.revocation = RevocationApi(api_client)
        self.schema = SchemaApi(api_client)
        self.server = ServerApi(api_client)
        self.settings = SettingsApi(api_client)
        self.trustping = TrustpingApi(api_client)
        self.wallet = WalletApi(api_client)
