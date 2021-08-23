import asyncio

import time

from aries_cloudcontroller.agent import get_aries_client

from aries_cloudcontroller import InvitationResult, ConnRecord, SendMessage


async def test():
    client = get_aries_client("http://localhost:10000", admin_insecure=True)

    # features = await client.server.get_features()
    invitation: InvitationResult = await client.connection.create_invitation()
    connection: ConnRecord = await client.connection.receive_invitation(
        body=invitation.invitation.dict(by_alias=True)
    )

    time.sleep(5)

    await client.basicmessage.send_message(
        conn_id=connection.connection_id, body=SendMessage(content="Hello")
    )


asyncio.get_event_loop().run_until_complete(test())
