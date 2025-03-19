import json
from aws import Cognito
from models import Connection, User, Context, Agent, Tool
from llm.AgentChatStream import AgentChatStream
from llm.CreateLLM import create_llm
from llm.BaseMessagesConverter import dict_messages_to_base_messages

async def handle_connect_to_context(data: dict, connection: Connection.Connection):

    # Set the user if access_token is provided
    access_token = data.get("access_token")
    user = None
    if access_token:
        cognito_user = Cognito.get_user_from_cognito(access_token)
        user = User.get_user(cognito_user.sub)

    # Get the context id
    context_id = data.get("context_id")
    if (context_id == None):
        raise Exception("No context_id provided")
    
    # Get the context
    context = None
    if (user):
        context = Context.get_context_for_user(context_id, user.user_id)
    else:
        context = Context.get_public_context(context_id)
    context_dict = context.model_dump()

    # Get the agent
    agent = None
    if (user):
        agent = Agent.get_agent_for_user(context.agent_id, user)
    else:
        agent = Agent.get_public_agent(context.agent_id)

    # Create the agent chat stream
    agent_chat = AgentChatStream(
        create_llm(),
        agent.prompt,
        messages=dict_messages_to_base_messages(context.messages),
        tools=[Tool.get_agent_tool_with_id(tool) for tool in agent.tools] if agent.tools else [],
        context=context_dict
    )

    # Set the connection's context and agent_chat
    connection.context = context
    connection.agent_chat = agent_chat

    # Send acknowledgement
    await connection.websocket.send(json.dumps({"type": "context_connected", "success": True}))
