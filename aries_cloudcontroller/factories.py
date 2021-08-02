from contextlib import asynccontextmanager

import aiohttp
import uplink
from aiohttp import ClientSession, TraceRequestChunkSentParams

from aries_cloudcontroller import AriesAgentController, AriesTenantController
from aries_cloudcontroller.api import WalletApi, SchemaApi
from aries_cloudcontroller.uplink import get_uplink


def get_aries_agent_controller(admin_url, api_key, is_multitenant=False):
    return AriesAgentController(
        admin_url=admin_url,
        api_key=api_key,
        is_multitenant=is_multitenant
    )


def get_aries_tenant_controller(admin_url, api_key, tenant_jwt, wallet_id):
    if not wallet_id:
        wallet_id = ''
    return AriesTenantController(
        admin_url=admin_url,
        api_key=api_key,
        tenant_jwt=tenant_jwt,
        wallet_id=wallet_id,
    )


def get_uplink_aries_controller(url, api_key, is_multitenant=False, tenant_jwt=None):
    """
       not differentiating between admin and regular as that is defined by the remote
       api and doe snot have to replicated here.
       Also separating the webhook context from this context as they are different responsibilities
    """
    return get_uplink(url, api_key, tenant_jwt=tenant_jwt)
