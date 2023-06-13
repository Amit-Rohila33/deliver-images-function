import asyncio
import aiohttp
import time
import os


class APISingleton:
    _instance = None
    _active_requests = 0

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = APISingleton()
        return cls._instance

    async def start_api(self):
        # Implementation of starting the API
        pass

    async def is_api_running(self):
        # Implementation of checking if the API is running
        pass

    async def finish_request(self):
        # Implementation of finishing the API request
        pass
    

# generate_images function implementation here
async def generate_images(session, payload):
    # Implementation of image generation logic
    pass


async def deliver_images(payload):
    api_singleton = APISingleton.get_instance()

    # Request to start the API
    await api_singleton.start_api()
    await api_singleton.is_api_running()  # Wait until the API is running

    timestamp = time.time()
    print(
        f"    {timestamp:.2f}: Starting generation. Number of active requests: {api_singleton._active_requests}")

    file_objects = []
    try:
        async with aiohttp.ClientSession() as session:
            task = generate_images(session, payload)
            file_objects = await asyncio.gather(task)  # This will be a list of lists
    finally:  # This ensures finish_request() is called even if an error occurs
        await api_singleton.finish_request()  # Indicate that the request is finished

    # Flatten the list and return
    print(f" {timestamp:.2f}: Image delivered. Number of active requests: {api_singleton._active_requests}")
    return [item for sublist in file_objects for item in sublist]


# This function should be executed in the serverless environment
def handler(event, context):
    payload = event['payload']
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(deliver_images(payload))
    return {'result': result}





# Sir, I have added a basic skeleton for the APISingleton class and the generate_images function. You have to fill in the actual implementation for these parts based on your requirements.


