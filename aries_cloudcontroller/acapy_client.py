from typing import Optional

from aiohttp.client import ClientSession

from aries_cloudcontroller.client import Client
from aries_cloudcontroller.util.create_client_session import create_client_session
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
            client_session = create_client_session(
                api_key=api_key, tenant_jwt=tenant_jwt
            )
            self._should_close_session = True

        self.client_session = client_session

        super().__init__(
            base_url,
            client=self.client_session,
            extra_service_params={"converter": PydanticConverter()},
        )

    async def __aexit__(self, exc_type, exc_value, traceback):
        if self._should_close_session and not self.client_session.closed:
            await self.client_session.close()
