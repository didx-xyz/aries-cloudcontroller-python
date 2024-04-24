# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.12.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr, validate_call
from typing_extensions import Annotated

from aries_cloudcontroller.api_client import ApiClient, RequestSerialized
from aries_cloudcontroller.models.invitation_create_request import (
    InvitationCreateRequest,
)
from aries_cloudcontroller.models.invitation_message import InvitationMessage
from aries_cloudcontroller.models.invitation_record import InvitationRecord
from aries_cloudcontroller.models.oob_record import OobRecord


class OutOfBandApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def create_invitation(
        self,
        auto_accept: Annotated[
            Optional[StrictBool],
            Field(description="Auto-accept connection (defaults to configuration)"),
        ] = None,
        create_unique_did: Annotated[
            Optional[StrictBool],
            Field(description="Create unique DID for this invitation (default false)"),
        ] = None,
        multi_use: Annotated[
            Optional[StrictBool],
            Field(description="Create invitation for multiple use (default false)"),
        ] = None,
        body: Optional[InvitationCreateRequest] = None,
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
    ) -> InvitationRecord:
        """Create a new connection invitation


        :param auto_accept: Auto-accept connection (defaults to configuration)
        :type auto_accept: bool
        :param create_unique_did: Create unique DID for this invitation (default false)
        :type create_unique_did: bool
        :param multi_use: Create invitation for multiple use (default false)
        :type multi_use: bool
        :param body:
        :type body: InvitationCreateRequest
        ...
        """  # noqa: E501

        _param = self._create_invitation_serialize(
            auto_accept=auto_accept,
            create_unique_did=create_unique_did,
            multi_use=multi_use,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "InvitationRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _create_invitation_serialize(
        self,
        auto_accept,
        create_unique_did,
        multi_use,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if auto_accept is not None:

            _query_params.append(("auto_accept", auto_accept))

        if create_unique_did is not None:

            _query_params.append(("create_unique_did", create_unique_did))

        if multi_use is not None:

            _query_params.append(("multi_use", multi_use))

        # process the header parameters
        # process the form parameters
        # process the body parameter
        if body is not None:
            _body_params = body

        # set the HTTP header `Accept`
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
            resource_path="/out-of-band/create-invitation",
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
    async def receive_invitation(
        self,
        alias: Annotated[
            Optional[StrictStr], Field(description="Alias for connection")
        ] = None,
        auto_accept: Annotated[
            Optional[StrictBool],
            Field(description="Auto-accept connection (defaults to configuration)"),
        ] = None,
        mediation_id: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Identifier for active mediation record to be used"),
        ] = None,
        use_existing_connection: Annotated[
            Optional[StrictBool],
            Field(description="Use an existing connection, if possible"),
        ] = None,
        body: Optional[InvitationMessage] = None,
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
    ) -> OobRecord:
        """Receive a new connection invitation


        :param alias: Alias for connection
        :type alias: str
        :param auto_accept: Auto-accept connection (defaults to configuration)
        :type auto_accept: bool
        :param mediation_id: Identifier for active mediation record to be used
        :type mediation_id: str
        :param use_existing_connection: Use an existing connection, if possible
        :type use_existing_connection: bool
        :param body:
        :type body: InvitationMessage
        ...
        """  # noqa: E501

        _param = self._receive_invitation_serialize(
            alias=alias,
            auto_accept=auto_accept,
            mediation_id=mediation_id,
            use_existing_connection=use_existing_connection,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "OobRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _receive_invitation_serialize(
        self,
        alias,
        auto_accept,
        mediation_id,
        use_existing_connection,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if alias is not None:

            _query_params.append(("alias", alias))

        if auto_accept is not None:

            _query_params.append(("auto_accept", auto_accept))

        if mediation_id is not None:

            _query_params.append(("mediation_id", mediation_id))

        if use_existing_connection is not None:

            _query_params.append(("use_existing_connection", use_existing_connection))

        # process the header parameters
        # process the form parameters
        # process the body parameter
        if body is not None:
            _body_params = body

        # set the HTTP header `Accept`
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
            resource_path="/out-of-band/receive-invitation",
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
    async def remove_invitation_record(
        self,
        invi_msg_id: Annotated[
            str, Field(strict=True, description="Invitation Message identifier")
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
    ) -> object:
        """Delete records associated with invitation


        :param invi_msg_id: Invitation Message identifier (required)
        :type invi_msg_id: str
        ...
        """  # noqa: E501

        _param = self._remove_invitation_record_serialize(
            invi_msg_id=invi_msg_id,
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

    def _remove_invitation_record_serialize(
        self,
        invi_msg_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if invi_msg_id is not None:
            _path_params["invi_msg_id"] = invi_msg_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]

        return self.api_client.param_serialize(
            method="DELETE",
            resource_path="/out-of-band/invitations/{invi_msg_id}",
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
