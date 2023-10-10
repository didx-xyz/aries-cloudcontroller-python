# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import re  # noqa: F401
import warnings
from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import Field, StrictStr, ValidationError, validate_call
from typing_extensions import Annotated

from aries_cloudcontroller.api_client import ApiClient
from aries_cloudcontroller.api_response import ApiResponse
from aries_cloudcontroller.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class IntroductionApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def start_introduction(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        target_connection_id: Annotated[StrictStr, Field(description="Target connection identifier")],
        message: Annotated[Optional[StrictStr], Field(description="Message")] = None,
        **kwargs,
    ) -> object:
        """Start an introduction between two connections  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.start_introduction(conn_id, target_connection_id, message, async_req=True)
        >>> result = thread.get()

        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param target_connection_id: Target connection identifier (required)
        :type target_connection_id: str
        :param message: Message
        :type message: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the start_introduction_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.start_introduction_with_http_info(conn_id, target_connection_id, message, **kwargs)  # noqa: E501

    @validate_call
    def start_introduction_with_http_info(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        target_connection_id: Annotated[StrictStr, Field(description="Target connection identifier")],
        message: Annotated[Optional[StrictStr], Field(description="Message")] = None,
        **kwargs,
    ) -> ApiResponse:
        """Start an introduction between two connections  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.start_introduction_with_http_info(conn_id, target_connection_id, message, async_req=True)
        >>> result = thread.get()

        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param target_connection_id: Target connection identifier (required)
        :type target_connection_id: str
        :param message: Message
        :type message: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'conn_id',
            'target_connection_id',
            'message'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_introduction" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['conn_id'] is not None:
            _path_params['conn_id'] = _params['conn_id']


        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get('target_connection_id') is not None:  # noqa: E501
            _query_params.append(('target_connection_id', _params['target_connection_id']))

        if _params.get('message') is not None:  # noqa: E501
            _query_params.append(('message', _params['message']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = ['AuthorizationHeader']  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }

        return self.api_client.call_api(
            '/connections/{conn_id}/start-introduction', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
