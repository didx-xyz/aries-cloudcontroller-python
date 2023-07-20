from typing import Optional

from aiohttp import ClientSession


class AcaPyClientSession:
    def __init__(self, api_key: Optional[str] = None, tenant_jwt: Optional[str] = None):
        headers = {}

        if api_key:
            headers["x-api-key"] = api_key
        if tenant_jwt:
            headers["authorization"] = f"Bearer {tenant_jwt}"

        self.client_session = ClientSession(
            headers=headers,
            raise_for_status=True,
        )

    async def __aenter__(self):
        return self.client_session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client_session.close()
