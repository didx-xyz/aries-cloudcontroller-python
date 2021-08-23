from typing import Optional
import aiohttp
from aiohttp.client import ClientSession
from aiohttp.tracing import TraceRequestChunkSentParams

from aries_cloudcontroller.client import Client
from aries_cloudcontroller.util.pydantic_converter import PydanticConverter


def get_aries_client(
    url,
    *,
    api_key: Optional[str] = None,
    tenant_jwt: Optional[str] = None,
    admin_insecure: bool = False,
):
    if not api_key and not admin_insecure:
        raise Exception(
            "api_key property is missing. Use admin_insecure=True if you want"
            " to use the controller without authentication."
        )

    headers = {}

    if api_key:
        headers["x-api-key"] = api_key
    if tenant_jwt:
        headers["authorization"] = f"Bearer {tenant_jwt}"

    client_session = get_client_session(headers)
    return Client(
        base_url=url,
        client=client_session,
        extra_service_params={"converter": PydanticConverter()},
    )


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


def get_client_session(headers):
    """need the async here as client session accesses the event loop..."""
    client_session = ClientSession(
        headers=headers,
        trace_configs=[trace_config],
        raise_for_status=True,
    )
    return client_session
