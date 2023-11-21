import asyncio

from aries_cloudcontroller import (
    AcaPyClient,
    ConnRecord,
    CreateInvitationRequest,
    InvitationResult,
    ReceiveInvitationRequest,
)

client = AcaPyClient(base_url="https://agent.community.animo.id", admin_insecure=True)


async def run():
    result: InvitationResult = await client.connection.create_invitation(
        body=CreateInvitationRequest(my_label="Cloud Controller")
    )

    # Pydantic v2 introduced strict model typing, so the InvitationResult must be converted to
    # a ReceiveInvitationRequest. These models share identical fields, and so can be converted:
    receive_invitation_request = ReceiveInvitationRequest.from_dict(
        result.invitation.to_dict()
    )

    connection: ConnRecord = await client.connection.receive_invitation(
        body=receive_invitation_request
    )

    print(connection)


asyncio.get_event_loop().run_until_complete(run())
