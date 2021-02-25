import asyncio

async def delay(func, seconds):
    await asyncio.sleep(seconds)
    func()