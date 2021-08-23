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

from aries_cloudcontroller.model.date import Date
from aries_cloudcontroller.model.endorser_info import EndorserInfo
from aries_cloudcontroller.model.transaction_jobs import TransactionJobs
from aries_cloudcontroller.model.transaction_list import TransactionList
from aries_cloudcontroller.model.transaction_record import TransactionRecord


class EndorseTransactionApi(Consumer):
    @returns.json
    @post("/transactions/{tran_id}/cancel")
    def cancel_transaction(self, *, tran_id: str) -> TransactionRecord:
        """For Author to cancel a particular transaction request"""

    @returns.json
    @json
    @post("/transactions/create-request")
    def create_request(self, *, tran_id: Query, endorser_write_txn: Query = None, body: Body(type=Date) = {}) -> TransactionRecord:
        """For author to send a transaction request"""

    @returns.json
    @post("/transactions/{tran_id}/endorse")
    def endorse_transaction(self, *, tran_id: str) -> TransactionRecord:
        """For Endorser to endorse a particular transaction record"""

    @returns.json
    @get("/transactions")
    def get_records(self) -> TransactionList:
        """Query transactions"""

    @returns.json
    @get("/transactions/{tran_id}")
    def get_transaction(self, *, tran_id: str) -> TransactionRecord:
        """Fetch a single transaction record"""

    @returns.json
    @post("/transactions/{tran_id}/refuse")
    def refuse_transaction(self, *, tran_id: str) -> TransactionRecord:
        """For Endorser to refuse a particular transaction record"""

    @returns.json
    @post("/transaction/{tran_id}/resend")
    def resend_transaction_request(self, *, tran_id: str) -> TransactionRecord:
        """For Author to resend a particular transaction request"""

    @returns.json
    @post("/transactions/{conn_id}/set-endorser-info")
    def set_endorser_info(self, *, conn_id: str, endorser_did: Query, endorser_name: Query = None) -> EndorserInfo:
        """Set Endorser Info"""

    @returns.json
    @post("/transactions/{conn_id}/set-endorser-role")
    def set_endorser_role(self, *, conn_id: str, transaction_my_job: Query = None) -> TransactionJobs:
        """Set transaction jobs"""

    @returns.json
    @post("/transactions/{tran_id}/write")
    def write_transaction(self, *, tran_id: str) -> TransactionRecord:
        """For Author / Endorser to write an endorsed transaction to the ledger"""

