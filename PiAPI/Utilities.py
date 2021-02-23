import asyncio

class Utilities:
    @staticmethod
    async def delay(func, seconds):
        await asyncio.sleep(seconds)
        func()
