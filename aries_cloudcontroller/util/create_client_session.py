from typing import Optional

from aiohttp import ClientSession


def create_client_session(
    api_key: Optional[str] = None, tenant_jwt: Optional[str] = None
):
    headers = {}

    if api_key:
        headers["x-api-key"] = api_key
    if tenant_jwt:
        headers["authorization"] = f"Bearer {tenant_jwt}"

    client_session = ClientSession(
        headers=headers,
        raise_for_status=True,
    )

    return client_session
