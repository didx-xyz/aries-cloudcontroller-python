# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.2.1.post20250228
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import Field, StrictFloat, StrictInt, StrictStr, validate_call
from typing_extensions import Annotated

from aries_cloudcontroller.api_client import ApiClient, RequestSerialized
from aries_cloudcontroller.models.get_schema_result import GetSchemaResult
from aries_cloudcontroller.models.get_schemas_response import GetSchemasResponse
from aries_cloudcontroller.models.schema_post_request import SchemaPostRequest
from aries_cloudcontroller.models.schema_result import SchemaResult


class AnoncredsSchemasApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def create_schema(
        self,
        body: Optional[SchemaPostRequest] = None,
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
    ) -> SchemaResult:
        """Create a schema on the connected datastore


        :param body:
        :type body: SchemaPostRequest
        ...
        """  # noqa: E501

        _param = self._create_schema_serialize(
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "SchemaResult",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _create_schema_serialize(
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
            resource_path="/anoncreds/schema",
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
    async def get_schema(
        self,
        schema_id: Annotated[StrictStr, Field(description="Schema identifier")],
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
    ) -> GetSchemaResult:
        """Retrieve an individual schemas details


        :param schema_id: Schema identifier (required)
        :type schema_id: str
        ...
        """  # noqa: E501

        _param = self._get_schema_serialize(
            schema_id=schema_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetSchemaResult",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_schema_serialize(
        self,
        schema_id,
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
        if schema_id is not None:
            _path_params["schema_id"] = schema_id
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
            resource_path="/anoncreds/schema/{schema_id}",
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
    async def get_schemas(
        self,
        schema_issuer_id: Annotated[
            Optional[StrictStr], Field(description="Schema issuer identifier")
        ] = None,
        schema_name: Annotated[
            Optional[StrictStr], Field(description="Schema name")
        ] = None,
        schema_version: Annotated[
            Optional[StrictStr], Field(description="Schema version")
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
    ) -> GetSchemasResponse:
        """Retrieve all schema ids


        :param schema_issuer_id: Schema issuer identifier
        :type schema_issuer_id: str
        :param schema_name: Schema name
        :type schema_name: str
        :param schema_version: Schema version
        :type schema_version: str
        ...
        """  # noqa: E501

        _param = self._get_schemas_serialize(
            schema_issuer_id=schema_issuer_id,
            schema_name=schema_name,
            schema_version=schema_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetSchemasResponse",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_schemas_serialize(
        self,
        schema_issuer_id,
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
        if schema_issuer_id is not None:

            _query_params.append(("schema_issuer_id", schema_issuer_id))

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
            resource_path="/anoncreds/schemas",
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
