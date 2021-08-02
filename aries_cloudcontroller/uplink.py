from contextlib import AbstractAsyncContextManager

import aiohttp
import uplink
from aiohttp import ClientSession, TraceRequestChunkSentParams
from uplink import AiohttpClient
from uplink.clients.interfaces import HttpClientAdapter

from aries_cloudcontroller.api import WalletApi, SchemaApi, ConnectionApi, ActionMenuApi, BasicmessageApi, \
    CredentialDefinitionApi, PresentProofV10Api, LedgerApi, ServerApi, OutOfBandApi, MediationApi, DidExchangeApi, \
    IssueCredentialV10Api, IssueCredentialV20Api, RevocationApi, MultitenancyApi


class UplinkAgent(AbstractAsyncContextManager):
    messaging: BasicmessageApi
    proofs: PresentProofV10Api
    ledger: LedgerApi
    connections: ConnectionApi
    server: ServerApi
    oob: OutOfBandApi
    mediation: MediationApi
    schema: SchemaApi
    wallet: WalletApi
    definitions: CredentialDefinitionApi
    didexchange: DidExchangeApi
    issuer_v2: IssueCredentialV20Api
    issuer = IssueCredentialV10Api
    action_menu: ActionMenuApi
    revocations: RevocationApi

    multitenant: MultitenancyApi

    def __init__(self, base_url: str, client: uplink.AiohttpClient):
        self.base_url = base_url
        # client = uplink.AiohttpClient(client_session)
        # client = client_session
        service_params = {"base_url": base_url, "client": client}
        self.wallet = WalletApi(**service_params)
        self.schema = SchemaApi(**service_params)
        self.proofs = PresentProofV10Api(**service_params)
        self.ledger = LedgerApi(**service_params)
        self.connections = ConnectionApi(**service_params)
        self.server = ServerApi(**service_params)
        self.oob = OutOfBandApi(**service_params)
        self.mediation = MediationApi(**service_params)
        self.schema = SchemaApi(**service_params)
        self.wallet = WalletApi(**service_params)
        self.definitions = CredentialDefinitionApi(**service_params)
        self.didexchange = DidExchangeApi(**service_params)
        self.issuer = IssueCredentialV10Api(**service_params)
        self.issuer_v2 = IssueCredentialV20Api(**service_params)
        self.action_menu = ActionMenuApi(**service_params)
        self.revocations = RevocationApi(**service_params)

        # always including the multi tenant api as whether it works or not
        # is based on whether the back end has it enabled. To simplify I'm not
        # going to toggle it here
        self.multitenant = MultitenancyApi(**service_params)
        self.client = client

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.client.close()

    async def close(self):
        await self.client.close()


async def on_request_start(session, context, params):
    print(f"Starting request <{params}>")


async def on_signal(session, context, params: TraceRequestChunkSentParams):
    print(f"chunk: <{params.chunk}>")


async def on_event(session, context, params):
    print(f"on event <{params}>")


trace_config = aiohttp.TraceConfig()
trace_config.on_request_start.append(on_request_start)
trace_config.on_request_chunk_sent.append(on_signal)
trace_config.on_response_chunk_received.append(on_signal)




def get_uplink(url, api_key, tenant_jwt=None):
    headers = {"x-api-key": api_key}
    if tenant_jwt:
        headers["authorization"] = f"Bearer {tenant_jwt}"

    client_session = get_client_session(headers)
    return UplinkAgent(base_url=url, client=client_session)


def get_client_session(headers):
    """ need the async here as client session accesses the event loop..."""
    client_session = ClientSession(
        headers=headers,
        trace_configs=[trace_config],
        raise_for_status=True,  # TODO would strongly prefer to manage my own erros as built in aiohttp swallows the
        # of an error. i.e. the _body_ of the http response is not included
    )
    return client_session


def get_uplink_(url, api_key, tenant_jwt=None):
    headers = {"x-api-key": api_key}
    if tenant_jwt:
        headers["authorization"] = f"Bearer {tenant_jwt}"

    # TODO would strongly prefer to manage my own erros as built in aiohttp swallows the
    # of an error. i.e. the _body_ of the http response is not included
    client = uplink.AiohttpClient(headers=headers,
            trace_configs=[trace_config],
            raise_for_status=True)
    return UplinkAgent(base_url=url, client=client)
        


