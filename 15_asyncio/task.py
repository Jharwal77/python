import asyncio

async def download():
    print("Downloading...")
    await asyncio.sleep(5)
    print("Done")

async def main():

    task = asyncio.create_task(download())

    print("Doing something else")

    await task

asyncio.run(main())