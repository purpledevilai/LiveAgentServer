from pydantic import BaseModel
from typing import Optional
from llm.AgentChatStream import AgentChatStream
from models import Context


class Connection(BaseModel):
    websocket: object
    context: Optional[Context.Context] = None
    agent_chat: Optional[AgentChatStream] = None

    model_config = {"arbitrary_types_allowed": True}  # Allow custom types