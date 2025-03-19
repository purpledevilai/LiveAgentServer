import json
from models import Connection, Context
from llm.BaseMessagesConverter import base_messages_to_dict_messages

async def handle_user_message(data: dict, connection: Connection.Connection):
    
    # Check that connection has context and agent_chat
    if (connection.context == None):
        raise Exception("No context set for connection")
    if (connection.agent_chat == None):
        raise Exception("No agent_chat set for connection")
    
    # Get the message
    message = data.get("message")
    if (message == None):
        raise Exception("No message provided")
    
    # Invoke the agent chat stream
    token_stream = connection.agent_chat.add_human_message_and_invoke(message)

    # Stream tokens
    for token in token_stream:
        await connection.websocket.send(json.dumps({"type": "message", "message": token}))

    # Save the new message to context
    context: Context.Context = connection.context
    context.messages = base_messages_to_dict_messages(connection.agent_chat.messages)
    Context.save_context(context)

    # check if there are chat events
    if (connection.agent_chat.context.get("events")):
        await connection.websocket.send(json.dumps({"type": "events", "events": connection.agent_chat.context["events"]}))
        connection.agent_chat.context["events"] = []
    