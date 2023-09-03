from typing import Any, Dict, List, Optional, Union  # noqa: F401

from uplink import (
    Body,
    Consumer,
    Header,
    Path,
    Query,
    delete,
    get,
    json,
    patch,
    post,
    put,
    returns,
)

from aries_cloudcontroller.uplink_util import bool_query


class DefaultApi(Consumer):
    async def get_features(self):
        """"""
        return await self.__get_features()

    @get("/features")
    def __get_features(self):
        """Internal uplink method for get_features"""
