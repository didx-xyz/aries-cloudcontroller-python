# coding: utf-8

"""
Aries Cloud Agent

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: v1.2.1.post20250213
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import Field, StrictFloat, StrictInt, StrictStr, validate_call
from typing_extensions import Annotated

from aries_cloudcontroller.api_client import ApiClient, RequestSerialized
from aries_cloudcontroller.models.endorser_info import EndorserInfo
from aries_cloudcontroller.models.model_date import ModelDate
from aries_cloudcontroller.models.transaction_jobs import TransactionJobs
from aries_cloudcontroller.models.transaction_list import TransactionList
from aries_cloudcontroller.models.transaction_record import TransactionRecord


class EndorseTransactionApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def cancel_transaction(
        self,
        tran_id: Annotated[StrictStr, Field(description="Transaction identifier")],
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
    ) -> TransactionRecord:
        """For Author to cancel a particular transaction request


        :param tran_id: Transaction identifier (required)
        :type tran_id: str
        ...
        """  # noqa: E501

        _param = self._cancel_transaction_serialize(
            tran_id=tran_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TransactionRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _cancel_transaction_serialize(
        self,
        tran_id,
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
        if tran_id is not None:
            _path_params["tran_id"] = tran_id
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
            resource_path="/transactions/{tran_id}/cancel",
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
    async def create_request(
        self,
        tran_id: Annotated[StrictStr, Field(description="Transaction identifier")],
        body: Optional[ModelDate] = None,
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
    ) -> TransactionRecord:
        """For author to send a transaction request


        :param tran_id: Transaction identifier (required)
        :type tran_id: str
        :param body:
        :type body: ModelDate
        ...
        """  # noqa: E501

        _param = self._create_request_serialize(
            tran_id=tran_id,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TransactionRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _create_request_serialize(
        self,
        tran_id,
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
        if tran_id is not None:

            _query_params.append(("tran_id", tran_id))

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
            resource_path="/transactions/create-request",
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
    async def endorse_transaction(
        self,
        tran_id: Annotated[StrictStr, Field(description="Transaction identifier")],
        endorser_did: Annotated[
            Optional[StrictStr], Field(description="Endorser DID")
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
    ) -> TransactionRecord:
        """For Endorser to endorse a particular transaction record


        :param tran_id: Transaction identifier (required)
        :type tran_id: str
        :param endorser_did: Endorser DID
        :type endorser_did: str
        ...
        """  # noqa: E501

        _param = self._endorse_transaction_serialize(
            tran_id=tran_id,
            endorser_did=endorser_did,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TransactionRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _endorse_transaction_serialize(
        self,
        tran_id,
        endorser_did,
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
        if tran_id is not None:
            _path_params["tran_id"] = tran_id
        # process the query parameters
        if endorser_did is not None:

            _query_params.append(("endorser_did", endorser_did))

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
            resource_path="/transactions/{tran_id}/endorse",
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
    async def get_records(
        self,
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
    ) -> TransactionList:
        """Query transactions


        ...
        """  # noqa: E501

        _param = self._get_records_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TransactionList",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_records_serialize(
        self,
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

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json"]
            )

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/transactions",
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
    async def get_transaction(
        self,
        tran_id: Annotated[StrictStr, Field(description="Transaction identifier")],
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
    ) -> TransactionRecord:
        """Fetch a single transaction record


        :param tran_id: Transaction identifier (required)
        :type tran_id: str
        ...
        """  # noqa: E501

        _param = self._get_transaction_serialize(
            tran_id=tran_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TransactionRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_transaction_serialize(
        self,
        tran_id,
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
        if tran_id is not None:
            _path_params["tran_id"] = tran_id
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
            resource_path="/transactions/{tran_id}",
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
    async def refuse_transaction(
        self,
        tran_id: Annotated[StrictStr, Field(description="Transaction identifier")],
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
    ) -> TransactionRecord:
        """For Endorser to refuse a particular transaction record


        :param tran_id: Transaction identifier (required)
        :type tran_id: str
        ...
        """  # noqa: E501

        _param = self._refuse_transaction_serialize(
            tran_id=tran_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TransactionRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _refuse_transaction_serialize(
        self,
        tran_id,
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
        if tran_id is not None:
            _path_params["tran_id"] = tran_id
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
            resource_path="/transactions/{tran_id}/refuse",
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
    async def resend_transaction_request(
        self,
        tran_id: Annotated[StrictStr, Field(description="Transaction identifier")],
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
    ) -> TransactionRecord:
        """For Author to resend a particular transaction request


        :param tran_id: Transaction identifier (required)
        :type tran_id: str
        ...
        """  # noqa: E501

        _param = self._resend_transaction_request_serialize(
            tran_id=tran_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TransactionRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _resend_transaction_request_serialize(
        self,
        tran_id,
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
        if tran_id is not None:
            _path_params["tran_id"] = tran_id
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
            resource_path="/transaction/{tran_id}/resend",
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
    async def set_endorser_info(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        endorser_did: Annotated[StrictStr, Field(description="Endorser DID")],
        endorser_name: Annotated[
            Optional[StrictStr], Field(description="Endorser Name")
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
    ) -> EndorserInfo:
        """Set Endorser Info


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param endorser_did: Endorser DID (required)
        :type endorser_did: str
        :param endorser_name: Endorser Name
        :type endorser_name: str
        ...
        """  # noqa: E501

        _param = self._set_endorser_info_serialize(
            conn_id=conn_id,
            endorser_did=endorser_did,
            endorser_name=endorser_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "EndorserInfo",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _set_endorser_info_serialize(
        self,
        conn_id,
        endorser_did,
        endorser_name,
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
        if endorser_did is not None:

            _query_params.append(("endorser_did", endorser_did))

        if endorser_name is not None:

            _query_params.append(("endorser_name", endorser_name))

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
            resource_path="/transactions/{conn_id}/set-endorser-info",
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
    async def set_endorser_role(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        transaction_my_job: Annotated[
            Optional[StrictStr], Field(description="Transaction related jobs")
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
    ) -> TransactionJobs:
        """Set transaction jobs


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param transaction_my_job: Transaction related jobs
        :type transaction_my_job: str
        ...
        """  # noqa: E501

        _param = self._set_endorser_role_serialize(
            conn_id=conn_id,
            transaction_my_job=transaction_my_job,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TransactionJobs",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _set_endorser_role_serialize(
        self,
        conn_id,
        transaction_my_job,
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
        if transaction_my_job is not None:

            _query_params.append(("transaction_my_job", transaction_my_job))

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
            resource_path="/transactions/{conn_id}/set-endorser-role",
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
    async def write_transaction(
        self,
        tran_id: Annotated[StrictStr, Field(description="Transaction identifier")],
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
    ) -> TransactionRecord:
        """For Author / Endorser to write an endorsed transaction to the ledger


        :param tran_id: Transaction identifier (required)
        :type tran_id: str
        ...
        """  # noqa: E501

        _param = self._write_transaction_serialize(
            tran_id=tran_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TransactionRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _write_transaction_serialize(
        self,
        tran_id,
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
        if tran_id is not None:
            _path_params["tran_id"] = tran_id
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
            resource_path="/transactions/{tran_id}/write",
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
