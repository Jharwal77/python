import asyncio

async def work():
    print("Start")

    await asyncio.sleep(3)

    print("End")

asyncio.run(work())