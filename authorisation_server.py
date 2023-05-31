import asyncio

async def authserv(s:str):
    print("Authorisation server is up and running")
    await asyncio.sleep(5)
    print("Auth server received")
    print(f"In the auth server, {s}")

    return 'Authorisation server data'
