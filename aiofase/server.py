import asyncio
import zmq
import zmq.asyncio as aiozmq


class Server:
    def __init__(self, sender_endpoint, receiver_endpoint):

        self.context = aiozmq.Context()

        self.receiver = self.context.socket(zmq.PULL)
        self.receiver.bind(receiver_endpoint)
        self.sender = self.context.socket(zmq.PUB)
        self.sender.bind(sender_endpoint)

    async def run(self):
        while True:
            data = await self.receiver.recv_string()
            self.sender.send_string(data, zmq.NOBLOCK)


if __name__ == '__main__':
    server = Server(sender_endpoint='ipc:///tmp/sender', receiver_endpoint='ipc:///tmp/receiver')
    asyncio.run(server.run())
