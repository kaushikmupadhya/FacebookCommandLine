import asyncio
import websockets

from threading import Thread
active = True
message = " "
async def send_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri, ping_interval=None) as websocket:
        #name = input("Enter your name : ")
        #print(name, " joined")
        while active:
            #print("Enter your message")
            #message = input()
            message = get_message()
            await websocket.send(message)

async def receive_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri, ping_interval=None) as websocket:
        while True:
            incoming_message = await websocket.recv()

def close_connection():
    active = False
    
def callback1():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_message())
    loop.close()

def callback2():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(receive_message())
    loop.close()

def user_message(msg):
    message = msg

def get_message():
    return message

_thread1 = Thread(target=callback1)
_thread2 = Thread(target=callback2)
_thread1.start()       
_thread2.start()       
