# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.2.0.post20241205
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr, validate_call
from typing_extensions import Annotated

from aries_cloudcontroller.api_client import ApiClient, RequestSerialized
from aries_cloudcontroller.models.credential_definition_get_result import (
    CredentialDefinitionGetResult,
)
from aries_cloudcontroller.models.credential_definition_send_request import (
    CredentialDefinitionSendRequest,
)
from aries_cloudcontroller.models.credential_definitions_created_result import (
    CredentialDefinitionsCreatedResult,
)
from aries_cloudcontroller.models.txn_or_credential_definition_send_result import (
    TxnOrCredentialDefinitionSendResult,
)


class CredentialDefinitionApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def fix_cred_def_wallet_record(
        self,
        cred_def_id: Annotated[
            str, Field(strict=True, description="Credential definition identifier")
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> CredentialDefinitionGetResult:
        """Writes a credential definition non-secret record to the wallet


        :param cred_def_id: Credential definition identifier (required)
        :type cred_def_id: str
        ...
        """  # noqa: E501

        _param = self._fix_cred_def_wallet_record_serialize(
            cred_def_id=cred_def_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "CredentialDefinitionGetResult",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _fix_cred_def_wallet_record_serialize(
        self,
        cred_def_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if cred_def_id is not None:
            _path_params["cred_def_id"] = cred_def_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json"]
            )

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/credential-definitions/{cred_def_id}/write_record",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    async def get_created_cred_defs(
        self,
        cred_def_id: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Credential definition id"),
        ] = None,
        issuer_did: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Issuer DID"),
        ] = None,
        schema_id: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Schema identifier"),
        ] = None,
        schema_issuer_did: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Schema issuer DID"),
        ] = None,
        schema_name: Annotated[
            Optional[StrictStr], Field(description="Schema name")
        ] = None,
        schema_version: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Schema version"),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> CredentialDefinitionsCreatedResult:
        """Search for matching credential definitions that agent originated


        :param cred_def_id: Credential definition id
        :type cred_def_id: str
        :param issuer_did: Issuer DID
        :type issuer_did: str
        :param schema_id: Schema identifier
        :type schema_id: str
        :param schema_issuer_did: Schema issuer DID
        :type schema_issuer_did: str
        :param schema_name: Schema name
        :type schema_name: str
        :param schema_version: Schema version
        :type schema_version: str
        ...
        """  # noqa: E501

        _param = self._get_created_cred_defs_serialize(
            cred_def_id=cred_def_id,
            issuer_did=issuer_did,
            schema_id=schema_id,
            schema_issuer_did=schema_issuer_did,
            schema_name=schema_name,
            schema_version=schema_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "CredentialDefinitionsCreatedResult",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_created_cred_defs_serialize(
        self,
        cred_def_id,
        issuer_did,
        schema_id,
        schema_issuer_did,
        schema_name,
        schema_version,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if cred_def_id is not None:

            _query_params.append(("cred_def_id", cred_def_id))

        if issuer_did is not None:

            _query_params.append(("issuer_did", issuer_did))

        if schema_id is not None:

            _query_params.append(("schema_id", schema_id))

        if schema_issuer_did is not None:

            _query_params.append(("schema_issuer_did", schema_issuer_did))

        if schema_name is not None:

            _query_params.append(("schema_name", schema_name))

        if schema_version is not None:

            _query_params.append(("schema_version", schema_version))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json"]
            )

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/credential-definitions/created",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    async def get_cred_def(
        self,
        cred_def_id: Annotated[
            str, Field(strict=True, description="Credential definition identifier")
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> CredentialDefinitionGetResult:
        """Gets a credential definition from the ledger


        :param cred_def_id: Credential definition identifier (required)
        :type cred_def_id: str
        ...
        """  # noqa: E501

        _param = self._get_cred_def_serialize(
            cred_def_id=cred_def_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "CredentialDefinitionGetResult",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_cred_def_serialize(
        self,
        cred_def_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if cred_def_id is not None:
            _path_params["cred_def_id"] = cred_def_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json"]
            )

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/credential-definitions/{cred_def_id}",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    async def publish_cred_def(
        self,
        conn_id: Annotated[
            Optional[StrictStr], Field(description="Connection identifier")
        ] = None,
        create_transaction_for_endorser: Annotated[
            Optional[StrictBool],
            Field(description="Create Transaction For Endorser's signature"),
        ] = None,
        body: Optional[CredentialDefinitionSendRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> TxnOrCredentialDefinitionSendResult:
        """Sends a credential definition to the ledger


        :param conn_id: Connection identifier
        :type conn_id: str
        :param create_transaction_for_endorser: Create Transaction For Endorser's signature
        :type create_transaction_for_endorser: bool
        :param body:
        :type body: CredentialDefinitionSendRequest
        ...
        """  # noqa: E501

        _param = self._publish_cred_def_serialize(
            conn_id=conn_id,
            create_transaction_for_endorser=create_transaction_for_endorser,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TxnOrCredentialDefinitionSendResult",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _publish_cred_def_serialize(
        self,
        conn_id,
        create_transaction_for_endorser,
        body,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if conn_id is not None:

            _query_params.append(("conn_id", conn_id))

        if create_transaction_for_endorser is not None:

            _query_params.append(
                ("create_transaction_for_endorser", create_transaction_for_endorser)
            )

        # process the header parameters
        # process the form parameters
        # process the body parameter
        if body is not None:
            _body_params = body

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json"]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/credential-definitions",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )
