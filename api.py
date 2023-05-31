import asyncio


async def fetch_data() -> str:
    print("fetching the data")
    await asyncio.sleep(5)
    print('Data fetched!')

    return 'API data'
