from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from models import Connection
from handle_message import handle_message

app = FastAPI()

# Optional: Add CORS if you expect to call from other domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend origin if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Connection opened")

    connection = Connection.Connection(websocket=websocket)

    try:
        while True:
            message = await websocket.receive_text()
            await handle_message(connection, message)
    except WebSocketDisconnect:
        print("Connection closed")
    except Exception as e:
        print("There was an error with the WebSocket connection:", e)
    finally:
        await websocket.close()
