import logging
import re

import pytest

from aries_cloudcontroller.acapy_client import AcaPyClient
from aries_cloudcontroller.util.acapy_client_session import AcaPyClientSession

LOGGER = logging.getLogger(__name__)


class TestAcaPyClient:
    admin_host = "http://localhost:1000"
    api_key = "api_key"
    tenant_jwt = "tenant_jwt"

    @pytest.mark.anyio
    async def test_init_acapy_client(self):
        async with AcaPyClient(self.admin_host, api_key=self.api_key) as client:
            assert type(client) is AcaPyClient

    @pytest.mark.anyio
    async def test_init_args_missing_api_key_no_insecure_mode(self):
        with pytest.raises(
            Exception,
            match=re.escape("api_key property is missing"),
        ):
            async with AcaPyClient(self.admin_host):
                pass

    @pytest.mark.anyio
    async def test_client_session_stays_open(self):
        async with AcaPyClientSession() as client_session:
            async with AcaPyClient(
                self.admin_host, client_session=client_session, admin_insecure=True
            ):
                pass
            # After AcaPyClient is closed, session should remain open
            assert client_session.closed is False

        # After async context is closed, session should be closed
        assert client_session.closed

    @pytest.mark.anyio
    async def test_client_session_closes_with_acapy(self):
        async with AcaPyClient(self.admin_host, admin_insecure=True) as acapy_client:
            # Check session is open within the AcaPyClient context
            assert acapy_client.client_session.closed is False

        # After AcaPyClient is closed, session should be closed
        assert acapy_client.client_session.closed is True

    @pytest.mark.anyio
    async def test_client_session_requires_api_key(self):
        with pytest.raises(
            Exception,
            match=re.escape("api_key property is missing"),
        ):
            async with AcaPyClientSession() as client_session:
                async with AcaPyClient(self.admin_host, client_session=client_session):
                    pass

    @pytest.mark.anyio
    async def test_client_session_creates_with_keys(self):
        async with AcaPyClient(
            self.admin_host, api_key=self.api_key, tenant_jwt=self.tenant_jwt
        ) as client:
            assert client.client_session.headers.get("x-api-key") == self.api_key
            assert (
                client.client_session.headers.get("authorization")
                == f"Bearer {self.tenant_jwt}"
            )
