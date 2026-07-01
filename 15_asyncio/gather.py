import asyncio

async def download(name, seconds):
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} completed")

async def main():

    await asyncio.gather(
        download("A", 5),
        download("B", 5)
    )

asyncio.run(main())