from pydantic import BaseModel
from typing import Optional
from llm.LiveChatAgent import LiveChatAgent
from models import Context


class Connection(BaseModel):
    websocket: object
    context: Optional[Context.Context] = None
    chat_agent: Optional[LiveChatAgent] = None

    model_config = {"arbitrary_types_allowed": True}  # Allow custom types