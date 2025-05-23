# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.3.0.post20250507
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr, validate_call
from typing_extensions import Annotated

from aries_cloudcontroller.api_client import ApiClient, RequestSerialized
from aries_cloudcontroller.models.conn_record import ConnRecord
from aries_cloudcontroller.models.connection_list import ConnectionList
from aries_cloudcontroller.models.connection_metadata import ConnectionMetadata
from aries_cloudcontroller.models.connection_metadata_set_request import (
    ConnectionMetadataSetRequest,
)
from aries_cloudcontroller.models.connection_static_request import (
    ConnectionStaticRequest,
)
from aries_cloudcontroller.models.connection_static_result import ConnectionStaticResult
from aries_cloudcontroller.models.endpoints_result import EndpointsResult


class ConnectionApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def create_static_connection(
        self,
        body: Optional[ConnectionStaticRequest] = None,
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
    ) -> ConnectionStaticResult:
        """Create a new static connection


        :param body:
        :type body: ConnectionStaticRequest
        ...
        """  # noqa: E501

        _param = self._create_static_connection_serialize(
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnectionStaticResult",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _create_static_connection_serialize(
        self,
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
            resource_path="/connections/create-static",
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
    async def delete_connection(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
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
    ) -> object:
        """Remove an existing connection record


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        ...
        """  # noqa: E501

        _param = self._delete_connection_serialize(
            conn_id=conn_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "object",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _delete_connection_serialize(
        self,
        conn_id,
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
        if conn_id is not None:
            _path_params["conn_id"] = conn_id
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
            method="DELETE",
            resource_path="/connections/{conn_id}",
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
    async def get_connection(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
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
    ) -> ConnRecord:
        """Fetch a single connection record


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        ...
        """  # noqa: E501

        _param = self._get_connection_serialize(
            conn_id=conn_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_connection_serialize(
        self,
        conn_id,
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
        if conn_id is not None:
            _path_params["conn_id"] = conn_id
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
            resource_path="/connections/{conn_id}",
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
    async def get_connection_endpoint(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
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
    ) -> EndpointsResult:
        """Fetch connection remote endpoint


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        ...
        """  # noqa: E501

        _param = self._get_connection_endpoint_serialize(
            conn_id=conn_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "EndpointsResult",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_connection_endpoint_serialize(
        self,
        conn_id,
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
        if conn_id is not None:
            _path_params["conn_id"] = conn_id
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
            resource_path="/connections/{conn_id}/endpoints",
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
    async def get_connections(
        self,
        alias: Annotated[Optional[StrictStr], Field(description="Alias")] = None,
        connection_protocol: Annotated[
            Optional[StrictStr], Field(description="Connection protocol used")
        ] = None,
        descending: Annotated[
            Optional[StrictBool],
            Field(description="Order results in descending order if true"),
        ] = None,
        invitation_key: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="invitation key"),
        ] = None,
        invitation_msg_id: Annotated[
            Optional[StrictStr],
            Field(description="Identifier of the associated Invitation Message"),
        ] = None,
        limit: Annotated[
            Optional[Annotated[int, Field(le=10000, strict=True, ge=1)]],
            Field(description="Number of results to return"),
        ] = None,
        my_did: Annotated[
            Optional[Annotated[str, Field(strict=True)]], Field(description="My DID")
        ] = None,
        offset: Annotated[
            Optional[Annotated[int, Field(strict=True, ge=0)]],
            Field(description="Offset for pagination"),
        ] = None,
        order_by: Annotated[
            Optional[StrictStr],
            Field(
                description='The column to order results by. Only "id" is currently supported.'
            ),
        ] = None,
        state: Annotated[
            Optional[StrictStr], Field(description="Connection state")
        ] = None,
        their_did: Annotated[
            Optional[Annotated[str, Field(strict=True)]], Field(description="Their DID")
        ] = None,
        their_public_did: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Their Public DID"),
        ] = None,
        their_role: Annotated[
            Optional[StrictStr],
            Field(description="Their role in the connection protocol"),
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
    ) -> ConnectionList:
        """Query agent-to-agent connections


        :param alias: Alias
        :type alias: str
        :param connection_protocol: Connection protocol used
        :type connection_protocol: str
        :param descending: Order results in descending order if true
        :type descending: bool
        :param invitation_key: invitation key
        :type invitation_key: str
        :param invitation_msg_id: Identifier of the associated Invitation Message
        :type invitation_msg_id: str
        :param limit: Number of results to return
        :type limit: int
        :param my_did: My DID
        :type my_did: str
        :param offset: Offset for pagination
        :type offset: int
        :param order_by: The column to order results by. Only \"id\" is currently supported.
        :type order_by: str
        :param state: Connection state
        :type state: str
        :param their_did: Their DID
        :type their_did: str
        :param their_public_did: Their Public DID
        :type their_public_did: str
        :param their_role: Their role in the connection protocol
        :type their_role: str
        ...
        """  # noqa: E501

        _param = self._get_connections_serialize(
            alias=alias,
            connection_protocol=connection_protocol,
            descending=descending,
            invitation_key=invitation_key,
            invitation_msg_id=invitation_msg_id,
            limit=limit,
            my_did=my_did,
            offset=offset,
            order_by=order_by,
            state=state,
            their_did=their_did,
            their_public_did=their_public_did,
            their_role=their_role,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnectionList",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_connections_serialize(
        self,
        alias,
        connection_protocol,
        descending,
        invitation_key,
        invitation_msg_id,
        limit,
        my_did,
        offset,
        order_by,
        state,
        their_did,
        their_public_did,
        their_role,
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
        if alias is not None:

            _query_params.append(("alias", alias))

        if connection_protocol is not None:

            _query_params.append(("connection_protocol", connection_protocol))

        if descending is not None:

            _query_params.append(("descending", descending))

        if invitation_key is not None:

            _query_params.append(("invitation_key", invitation_key))

        if invitation_msg_id is not None:

            _query_params.append(("invitation_msg_id", invitation_msg_id))

        if limit is not None:

            _query_params.append(("limit", limit))

        if my_did is not None:

            _query_params.append(("my_did", my_did))

        if offset is not None:

            _query_params.append(("offset", offset))

        if order_by is not None:

            _query_params.append(("order_by", order_by))

        if state is not None:

            _query_params.append(("state", state))

        if their_did is not None:

            _query_params.append(("their_did", their_did))

        if their_public_did is not None:

            _query_params.append(("their_public_did", their_public_did))

        if their_role is not None:

            _query_params.append(("their_role", their_role))

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
            resource_path="/connections",
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
    async def get_metadata(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        key: Annotated[
            Optional[StrictStr], Field(description="Key to retrieve.")
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
    ) -> ConnectionMetadata:
        """Fetch connection metadata


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param key: Key to retrieve.
        :type key: str
        ...
        """  # noqa: E501

        _param = self._get_metadata_serialize(
            conn_id=conn_id,
            key=key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnectionMetadata",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_metadata_serialize(
        self,
        conn_id,
        key,
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
        if conn_id is not None:
            _path_params["conn_id"] = conn_id
        # process the query parameters
        if key is not None:

            _query_params.append(("key", key))

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
            resource_path="/connections/{conn_id}/metadata",
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
    async def set_metadata(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        body: Optional[ConnectionMetadataSetRequest] = None,
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
    ) -> ConnectionMetadata:
        """Set connection metadata


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param body:
        :type body: ConnectionMetadataSetRequest
        ...
        """  # noqa: E501

        _param = self._set_metadata_serialize(
            conn_id=conn_id,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnectionMetadata",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _set_metadata_serialize(
        self,
        conn_id,
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
        if conn_id is not None:
            _path_params["conn_id"] = conn_id
        # process the query parameters
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
            resource_path="/connections/{conn_id}/metadata",
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
