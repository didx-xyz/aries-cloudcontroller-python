from uplink import (
    Consumer,
    get,
    Path,
    Query,
    Body,
    post,
    get,
    patch,
    put,
    delete,
    Header,
    returns,
    json,
)

from typing import Dict, List  # noqa: F401

from aries_cloudcontroller.model.attribute_mime_types_result import AttributeMimeTypesResult
from aries_cloudcontroller.model.cred_info_list import CredInfoList
from aries_cloudcontroller.model.cred_revoked_result import CredRevokedResult
from aries_cloudcontroller.model.indy_cred_info import IndyCredInfo
from aries_cloudcontroller.model.vc_record import VCRecord
from aries_cloudcontroller.model.vc_record_list import VCRecordList
from aries_cloudcontroller.model.w3_c_credentials_list_request import W3CCredentialsListRequest


class CredentialsApi(Consumer):
    @returns.json
    @delete("/credential/{credential_id}")
    def delete_record(self, *, credential_id: str) -> Dict:
        """Remove credential from wallet by id"""

    @returns.json
    @delete("/credential/w3c/{credential_id}")
    def delete_w3c_credential(self, *, credential_id: str) -> Dict:
        """Remove W3C credential from wallet by id"""

    @returns.json
    @get("/credential/mime-types/{credential_id}")
    def get_credential_mime_types(self, *, credential_id: str) -> AttributeMimeTypesResult:
        """Get attribute MIME types from wallet"""

    @returns.json
    @get("/credential/{credential_id}")
    def get_record(self, *, credential_id: str) -> IndyCredInfo:
        """Fetch credential from wallet by id"""

    @returns.json
    @get("/credentials")
    def get_records(self, *, count: Query = None, start: Query = None, wql: Query = None) -> CredInfoList:
        """Fetch credentials from wallet"""

    @returns.json
    @get("/credential/revoked/{credential_id}")
    def get_revocation_status(self, *, credential_id: str, from_: Query = None, to: Query = None) -> CredRevokedResult:
        """Query credential revocation status by id"""

    @returns.json
    @get("/credential/w3c/{credential_id}")
    def get_w3c_credential(self, *, credential_id: str) -> VCRecord:
        """Fetch W3C credential from wallet by id"""

    @returns.json
    @json
    @post("/credentials/w3c")
    def get_w3c_credentials(self, *, count: Query = None, start: Query = None, wql: Query = None, body: Body(type=W3CCredentialsListRequest) = {}) -> VCRecordList:
        """Fetch W3C credentials from wallet"""

