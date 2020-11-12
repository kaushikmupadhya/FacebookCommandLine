from websocket_server import WebsocketServer

queue = [] 
# Called for every client connecting (after handshake)
def new_client(client, server):
	# print("New client connected and was given id %d" % client['id'])
	# server.send_message_to_all("Hey all, a new client has joined us")
    for i in queue:
        server.send_message_to_all(i)
    pass


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
    if len(queue) == 9:
        queue.pop(0)
        queue.append(message)
    else:
        queue.append(message)
    if len(message) > 200:
        message = message[:200]+'..'
    print("Client(%d) said: %s" % (client['id'], message))
    server.send_message_to_all(message)
    


PORT=8765
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
