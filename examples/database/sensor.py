from aiofase.microservice import MicroService

import asyncio
import random


class EnergySensor(MicroService):
    def __init__(self) -> None:
        super().__init__(self, sender_endpoint='ipc:///tmp/sender', receiver_endpoint='ipc:///tmp/receiver')

    async def on_connect(self):
        print('### on_connect ###')

    async def on_new_service(self, service, actions):
        print('### on_new_service ### service: %s - actions: %s' % (service, actions))

    async def on_response(self, service, data):
        print('### on_response ### service: %s respond an status of the action save_data previous resquested: %s' % (service, data))

    @MicroService.task
    async def meter_process(self):
        while True:
            sensor_data = random.randrange(10, 50, 1)
            await self.request_action('save_data', {'sensor': sensor_data})
            
            await asyncio.sleep(2)


if __name__ == '__main__':
    sensor = EnergySensor()
    asyncio.run(sensor.run())
