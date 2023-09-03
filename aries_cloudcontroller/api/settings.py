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

from aries_cloudcontroller.model.profile_settings import ProfileSettings
from aries_cloudcontroller.model.update_profile_settings import UpdateProfileSettings
from aries_cloudcontroller.uplink_util import bool_query


class SettingsApi(Consumer):
    async def settings_get(self) -> ProfileSettings:
        """Get the configurable settings associated with the profile."""
        return await self.__settings_get()

    async def settings_put(
        self, *, body: Optional[UpdateProfileSettings] = None
    ) -> ProfileSettings:
        """Update configurable settings associated with the profile."""
        if not body:
            body = UpdateProfileSettings()
        return await self.__settings_put(
            body=body,
        )

    @returns.json
    @get("/settings")
    def __settings_get(self) -> ProfileSettings:
        """Internal uplink method for settings_get"""

    @returns.json
    @json
    @put("/settings")
    def __settings_put(
        self, *, body: Body(type=UpdateProfileSettings) = {}
    ) -> ProfileSettings:
        """Internal uplink method for settings_put"""
