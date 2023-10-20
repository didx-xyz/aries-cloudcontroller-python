# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from typing import Dict, List, Optional, Tuple

from pydantic import Field, StrictBool, StrictStr, validate_call
from typing_extensions import Annotated

from aries_cloudcontroller.api_client import ApiClient
from aries_cloudcontroller.api_response import ApiResponse
from aries_cloudcontroller.exceptions import ApiTypeError
from aries_cloudcontroller.models.conn_record import ConnRecord
from aries_cloudcontroller.models.didx_request import DIDXRequest


class DidExchangeApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def accept_invitation(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        my_endpoint: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="My URL endpoint"),
        ] = None,
        my_label: Annotated[
            Optional[StrictStr], Field(description="Label for connection request")
        ] = None,
        **kwargs,
    ) -> ConnRecord:
        """Accept a stored connection invitation  # noqa: E501


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param my_endpoint: My URL endpoint
        :type my_endpoint: str
        :param my_label: Label for connection request
        :type my_label: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ConnRecord
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the accept_invitation_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.accept_invitation_with_http_info.raw_function(
            conn_id,
            my_endpoint,
            my_label,
            **kwargs,
        )

    @validate_call
    async def accept_invitation_with_http_info(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        my_endpoint: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="My URL endpoint"),
        ] = None,
        my_label: Annotated[
            Optional[StrictStr], Field(description="Label for connection request")
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        """Accept a stored connection invitation  # noqa: E501


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param my_endpoint: My URL endpoint
        :type my_endpoint: str
        :param my_label: Label for connection request
        :type my_label: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ConnRecord, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["conn_id", "my_endpoint", "my_label"]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method accept_invitation" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params["conn_id"] is not None:
            _path_params["conn_id"] = _params["conn_id"]

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get("my_endpoint") is not None:  # noqa: E501
            _query_params.append(("my_endpoint", _params["my_endpoint"]))

        if _params.get("my_label") is not None:  # noqa: E501
            _query_params.append(("my_label", _params["my_label"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnRecord",
        }

        return await self.api_client.call_api(
            "/didexchange/{conn_id}/accept-invitation",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_call
    async def accept_request(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        mediation_id: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Identifier for active mediation record to be used"),
        ] = None,
        my_endpoint: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="My URL endpoint"),
        ] = None,
        **kwargs,
    ) -> ConnRecord:
        """Accept a stored connection request  # noqa: E501


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param mediation_id: Identifier for active mediation record to be used
        :type mediation_id: str
        :param my_endpoint: My URL endpoint
        :type my_endpoint: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ConnRecord
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the accept_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.accept_request_with_http_info.raw_function(
            conn_id,
            mediation_id,
            my_endpoint,
            **kwargs,
        )

    @validate_call
    async def accept_request_with_http_info(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        mediation_id: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Identifier for active mediation record to be used"),
        ] = None,
        my_endpoint: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="My URL endpoint"),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        """Accept a stored connection request  # noqa: E501


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param mediation_id: Identifier for active mediation record to be used
        :type mediation_id: str
        :param my_endpoint: My URL endpoint
        :type my_endpoint: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ConnRecord, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["conn_id", "mediation_id", "my_endpoint"]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method accept_request" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params["conn_id"] is not None:
            _path_params["conn_id"] = _params["conn_id"]

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get("mediation_id") is not None:  # noqa: E501
            _query_params.append(("mediation_id", _params["mediation_id"]))

        if _params.get("my_endpoint") is not None:  # noqa: E501
            _query_params.append(("my_endpoint", _params["my_endpoint"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnRecord",
        }

        return await self.api_client.call_api(
            "/didexchange/{conn_id}/accept-request",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_call
    async def create_request(
        self,
        their_public_did: Annotated[
            str,
            Field(
                strict=True,
                description="Qualified public DID to which to request connection",
            ),
        ],
        alias: Annotated[
            Optional[StrictStr], Field(description="Alias for connection")
        ] = None,
        goal: Annotated[
            Optional[StrictStr],
            Field(
                description="A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message"
            ),
        ] = None,
        goal_code: Annotated[
            Optional[StrictStr],
            Field(
                description="A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message"
            ),
        ] = None,
        mediation_id: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Identifier for active mediation record to be used"),
        ] = None,
        my_endpoint: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="My URL endpoint"),
        ] = None,
        my_label: Annotated[
            Optional[StrictStr], Field(description="Label for connection request")
        ] = None,
        use_public_did: Annotated[
            Optional[StrictBool],
            Field(description="Use public DID for this connection"),
        ] = None,
        **kwargs,
    ) -> ConnRecord:
        """Create and send a request against public DID's implicit invitation  # noqa: E501


        :param their_public_did: Qualified public DID to which to request connection (required)
        :type their_public_did: str
        :param alias: Alias for connection
        :type alias: str
        :param goal: A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message
        :type goal: str
        :param goal_code: A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message
        :type goal_code: str
        :param mediation_id: Identifier for active mediation record to be used
        :type mediation_id: str
        :param my_endpoint: My URL endpoint
        :type my_endpoint: str
        :param my_label: Label for connection request
        :type my_label: str
        :param use_public_did: Use public DID for this connection
        :type use_public_did: bool
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ConnRecord
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.create_request_with_http_info.raw_function(
            their_public_did,
            alias,
            goal,
            goal_code,
            mediation_id,
            my_endpoint,
            my_label,
            use_public_did,
            **kwargs,
        )

    @validate_call
    async def create_request_with_http_info(
        self,
        their_public_did: Annotated[
            str,
            Field(
                strict=True,
                description="Qualified public DID to which to request connection",
            ),
        ],
        alias: Annotated[
            Optional[StrictStr], Field(description="Alias for connection")
        ] = None,
        goal: Annotated[
            Optional[StrictStr],
            Field(
                description="A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message"
            ),
        ] = None,
        goal_code: Annotated[
            Optional[StrictStr],
            Field(
                description="A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message"
            ),
        ] = None,
        mediation_id: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Identifier for active mediation record to be used"),
        ] = None,
        my_endpoint: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="My URL endpoint"),
        ] = None,
        my_label: Annotated[
            Optional[StrictStr], Field(description="Label for connection request")
        ] = None,
        use_public_did: Annotated[
            Optional[StrictBool],
            Field(description="Use public DID for this connection"),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        """Create and send a request against public DID's implicit invitation  # noqa: E501


        :param their_public_did: Qualified public DID to which to request connection (required)
        :type their_public_did: str
        :param alias: Alias for connection
        :type alias: str
        :param goal: A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message
        :type goal: str
        :param goal_code: A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message
        :type goal_code: str
        :param mediation_id: Identifier for active mediation record to be used
        :type mediation_id: str
        :param my_endpoint: My URL endpoint
        :type my_endpoint: str
        :param my_label: Label for connection request
        :type my_label: str
        :param use_public_did: Use public DID for this connection
        :type use_public_did: bool
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ConnRecord, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            "their_public_did",
            "alias",
            "goal",
            "goal_code",
            "mediation_id",
            "my_endpoint",
            "my_label",
            "use_public_did",
        ]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_request" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get("their_public_did") is not None:  # noqa: E501
            _query_params.append(("their_public_did", _params["their_public_did"]))

        if _params.get("alias") is not None:  # noqa: E501
            _query_params.append(("alias", _params["alias"]))

        if _params.get("goal") is not None:  # noqa: E501
            _query_params.append(("goal", _params["goal"]))

        if _params.get("goal_code") is not None:  # noqa: E501
            _query_params.append(("goal_code", _params["goal_code"]))

        if _params.get("mediation_id") is not None:  # noqa: E501
            _query_params.append(("mediation_id", _params["mediation_id"]))

        if _params.get("my_endpoint") is not None:  # noqa: E501
            _query_params.append(("my_endpoint", _params["my_endpoint"]))

        if _params.get("my_label") is not None:  # noqa: E501
            _query_params.append(("my_label", _params["my_label"]))

        if _params.get("use_public_did") is not None:  # noqa: E501
            _query_params.append(("use_public_did", _params["use_public_did"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnRecord",
        }

        return await self.api_client.call_api(
            "/didexchange/create-request",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_call
    async def receive_request(
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
        my_endpoint: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="My URL endpoint"),
        ] = None,
        body: Optional[DIDXRequest] = None,
        **kwargs,
    ) -> ConnRecord:
        """Receive request against public DID's implicit invitation  # noqa: E501


        :param alias: Alias for connection
        :type alias: str
        :param auto_accept: Auto-accept connection (defaults to configuration)
        :type auto_accept: bool
        :param mediation_id: Identifier for active mediation record to be used
        :type mediation_id: str
        :param my_endpoint: My URL endpoint
        :type my_endpoint: str
        :param body:
        :type body: DIDXRequest
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ConnRecord
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the receive_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.receive_request_with_http_info.raw_function(
            alias,
            auto_accept,
            mediation_id,
            my_endpoint,
            body,
            **kwargs,
        )

    @validate_call
    async def receive_request_with_http_info(
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
        my_endpoint: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="My URL endpoint"),
        ] = None,
        body: Optional[DIDXRequest] = None,
        **kwargs,
    ) -> ApiResponse:
        """Receive request against public DID's implicit invitation  # noqa: E501


        :param alias: Alias for connection
        :type alias: str
        :param auto_accept: Auto-accept connection (defaults to configuration)
        :type auto_accept: bool
        :param mediation_id: Identifier for active mediation record to be used
        :type mediation_id: str
        :param my_endpoint: My URL endpoint
        :type my_endpoint: str
        :param body:
        :type body: DIDXRequest
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ConnRecord, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["alias", "auto_accept", "mediation_id", "my_endpoint", "body"]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method receive_request" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get("alias") is not None:  # noqa: E501
            _query_params.append(("alias", _params["alias"]))

        if _params.get("auto_accept") is not None:  # noqa: E501
            _query_params.append(("auto_accept", _params["auto_accept"]))

        if _params.get("mediation_id") is not None:  # noqa: E501
            _query_params.append(("mediation_id", _params["mediation_id"]))

        if _params.get("my_endpoint") is not None:  # noqa: E501
            _query_params.append(("my_endpoint", _params["my_endpoint"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        if _params["body"] is not None:
            _body_params = _params["body"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnRecord",
        }

        return await self.api_client.call_api(
            "/didexchange/receive-request",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
