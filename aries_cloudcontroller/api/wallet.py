from uplink import (
    Consumer,
    Path,
    Query,
    Body,
    Header,
    get,
    post,
    patch,
    put,
    delete,
    returns,
    json,
)

from typing import Any, Dict, List, Optional, Union  # noqa: F401

from aries_cloudcontroller.uplink_util import bool_query

from aries_cloudcontroller.model.did_create import DIDCreate
from aries_cloudcontroller.model.did_endpoint import DIDEndpoint
from aries_cloudcontroller.model.did_endpoint_with_type import DIDEndpointWithType
from aries_cloudcontroller.model.did_list import DIDList
from aries_cloudcontroller.model.did_result import DIDResult
from aries_cloudcontroller.model.jws_create import JWSCreate
from aries_cloudcontroller.model.jws_verify import JWSVerify
from aries_cloudcontroller.model.jws_verify_response import JWSVerifyResponse


class WalletApi(Consumer):
    async def create_did(self, *, body: Optional[DIDCreate] = None) -> DIDResult:
        """Create a local DID"""
        if not body:
            body = DIDCreate()
        return await self.__create_did(
            body=body,
        )

    async def get_did_endpoint(self, *, did: str) -> DIDEndpoint:
        """Query DID endpoint in wallet"""
        return await self.__get_did_endpoint(
            did=did,
        )

    async def get_dids(
        self,
        *,
        did: Optional[str] = None,
        key_type: Optional[str] = None,
        method: Optional[str] = None,
        posture: Optional[str] = None,
        verkey: Optional[str] = None
    ) -> DIDList:
        """List wallet DIDs"""
        return await self.__get_dids(
            did=did,
            key_type=key_type,
            method=method,
            posture=posture,
            verkey=verkey,
        )

    async def get_public_did(self) -> DIDResult:
        """Fetch the current public DID"""
        return await self.__get_public_did()

    async def rotate_keypair(self, *, did: str) -> Dict[str, Any]:
        """Rotate keypair for a DID not posted to the ledger"""
        return await self.__rotate_keypair(
            did=did,
        )

    async def set_did_endpoint(
        self,
        *,
        conn_id: Optional[str] = None,
        create_transaction_for_endorser: Optional[bool] = None,
        body: Optional[DIDEndpointWithType] = None
    ) -> Dict[str, Any]:
        """Update endpoint in wallet and on ledger if posted to it"""
        if not body:
            body = DIDEndpointWithType()
        return await self.__set_did_endpoint(
            conn_id=conn_id,
            create_transaction_for_endorser=bool_query(create_transaction_for_endorser),
            body=body,
        )

    async def set_public_did(
        self,
        *,
        did: str,
        conn_id: Optional[str] = None,
        create_transaction_for_endorser: Optional[bool] = None,
        mediation_id: Optional[str] = None
    ) -> DIDResult:
        """Assign the current public DID"""
        return await self.__set_public_did(
            did=did,
            conn_id=conn_id,
            create_transaction_for_endorser=bool_query(create_transaction_for_endorser),
            mediation_id=mediation_id,
        )

    async def wallet_jwt_sign_post(
        self, *, body: Optional[JWSCreate] = None
    ) -> Dict[str, Any]:
        """Create a EdDSA jws using did keys with a given payload"""
        if not body:
            body = JWSCreate()
        return await self.__wallet_jwt_sign_post(
            body=body,
        )

    async def wallet_jwt_verify_post(
        self, *, body: Optional[JWSVerify] = None
    ) -> JWSVerifyResponse:
        """Verify a EdDSA jws using did keys with a given JWS"""
        if not body:
            body = JWSVerify()
        return await self.__wallet_jwt_verify_post(
            body=body,
        )

    @returns.json
    @json
    @post("/wallet/did/create")
    def __create_did(self, *, body: Body(type=DIDCreate) = {}) -> DIDResult:
        """Internal uplink method for create_did"""

    @returns.json
    @get("/wallet/get-did-endpoint")
    def __get_did_endpoint(self, *, did: Query) -> DIDEndpoint:
        """Internal uplink method for get_did_endpoint"""

    @returns.json
    @get("/wallet/did")
    def __get_dids(
        self,
        *,
        did: Query = None,
        key_type: Query = None,
        method: Query = None,
        posture: Query = None,
        verkey: Query = None
    ) -> DIDList:
        """Internal uplink method for get_dids"""

    @returns.json
    @get("/wallet/did/public")
    def __get_public_did(self) -> DIDResult:
        """Internal uplink method for get_public_did"""

    @returns.json
    @patch("/wallet/did/local/rotate-keypair")
    def __rotate_keypair(self, *, did: Query) -> Dict[str, Any]:
        """Internal uplink method for rotate_keypair"""

    @returns.json
    @json
    @post("/wallet/set-did-endpoint")
    def __set_did_endpoint(
        self,
        *,
        conn_id: Query = None,
        create_transaction_for_endorser: Query = None,
        body: Body(type=DIDEndpointWithType) = {}
    ) -> Dict[str, Any]:
        """Internal uplink method for set_did_endpoint"""

    @returns.json
    @post("/wallet/did/public")
    def __set_public_did(
        self,
        *,
        did: Query,
        conn_id: Query = None,
        create_transaction_for_endorser: Query = None,
        mediation_id: Query = None
    ) -> DIDResult:
        """Internal uplink method for set_public_did"""

    @returns.json
    @json
    @post("/wallet/jwt/sign")
    def __wallet_jwt_sign_post(
        self, *, body: Body(type=JWSCreate) = {}
    ) -> Dict[str, Any]:
        """Internal uplink method for wallet_jwt_sign_post"""

    @returns.json
    @json
    @post("/wallet/jwt/verify")
    def __wallet_jwt_verify_post(
        self, *, body: Body(type=JWSVerify) = {}
    ) -> JWSVerifyResponse:
        """Internal uplink method for wallet_jwt_verify_post"""
