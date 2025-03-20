import json
from models import Connection
from handlers.handle_connect_to_context import handle_connect_to_context
from handlers.handle_user_message import handle_user_message

async def route_message(type: str, data: dict, connection: Connection.Connection):

    #################################################
    #
    #
    # -- Connect to context
    if (type == "connect_to_context"):
        await handle_connect_to_context(data, connection)
    #
    #
    # -- Message
    elif (type == "message"):
        await handle_user_message(data, connection)
    #
    #
    # -- Invalid message type
    else:
        raise Exception(f"Invalid message type: {type}")
    #
    #
    #
    #####################################################


async def handle_message(connection: Connection.Connection, message: str):
    try:
        # Parse the JSON message
        data = json.loads(message)

        # Get the message type
        type = data.get("type")
        if (type == None):
            raise Exception("No type provided")

        # Route message
        await route_message(type, data, connection)

    except Exception as e:
        print(f"Error: {e}")
        await connection.websocket.send(json.dumps({"type": "error", "error": str(e)}))
