from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel

## connect with bash:
## websocat ws://your_server/url

app = FastAPI()
websocket_clients = []


class Message(BaseModel):
    text: str


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received from WebSocket: {data}")
            ## i have to do some filter
            for client in websocket_clients:
                client.send_text(data)
    except WebSocketDisconnect:
        websocket_clients.remove(websocket)
    except Exception as e:
        print(e)
    return


@app.post("/send-message")
async def send_message(message: Message):
    # Broadcast the received message to all connected WebSocket clients
    for client in websocket_clients:
        await client.send_text(f"Message received from POST request: {message.text}")
    return {"message": f"Broadcast message to all WebSocket clients: {message.text}"}
