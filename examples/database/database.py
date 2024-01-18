from aiofase.microservice import MicroService


import asyncio


class Database(MicroService):
    def __init__(self):
        super().__init__(self, sender_endpoint='ipc:///tmp/sender', receiver_endpoint='ipc:///tmp/receiver')

    async def on_connect(self):
        print('### on_connect ###')
        await self.send_broadcast({'message': 'database service is online'})

    async def on_new_service(self, service, actions):
        print('### on_new_service ### service: %s - actions: %s' % (service, actions))

    @MicroService.action
    async def save_data(self, service, data):
        print('### action::save_data: %s ' % data)
        # save some data on database and respond a status to requester 'service'
        await self.response(service, {'save_data_ack': {'status': 'saved'}})


if __name__ == '__main__':
    database = Database()
    asyncio.run(database.run())
