from typing import Optional

from aiohttp.client import ClientSession

from aries_cloudcontroller.client import Client
from aries_cloudcontroller.util.acapy_client_session import AcaPyClientSession
from aries_cloudcontroller.util.pydantic_converter import PydanticConverter


class AcaPyClient(Client):
    def __init__(
        self,
        base_url: str,
        *,
        client_session: Optional[ClientSession] = None,
        api_key: Optional[str] = None,
        admin_insecure: Optional[bool] = False,
        tenant_jwt: Optional[str] = None,
    ):
        self.base_url = base_url

        self._should_close_session = False  # only close ClientSession when created here
        # A provided ClientSession should be closed externally.

        if client_session and not api_key:
            api_key = client_session.headers.get("x-api-key")

        if not api_key and not admin_insecure:
            raise Exception(
                "api_key property is missing. Use admin_insecure=True if you want"
                " to use the controller without authentication."
            )

        if not client_session:
            self.client_session = AcaPyClientSession(
                api_key=api_key, tenant_jwt=tenant_jwt
            ).client_session
            self._should_close_session = True
        else:
            self.client_session = client_session

        super().__init__(
            self.base_url,
            client=self.client_session,
            extra_service_params={"converter": PydanticConverter()},
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        if self._should_close_session and not self.client_session.closed:
            await self.client_session.close()
