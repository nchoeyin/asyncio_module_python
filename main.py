import asyncio
import api
import authorisation_server

async def send_data(to: str):
    print(f"Sending data to {to}.....")
    await asyncio.sleep(5)
    print(f"Data sent to {to}!")

async def main():
    data = await api.fetch_data()
    print('Data:', data)
    await asyncio.gather(send_data('Lebron'), send_data('Jordan')) #The keyword gather makes all the functions work in simultaneously in asynchronous manner
    await authorisation_server.authserv('Cristiano')

if __name__ == '__main__':
    asyncio.run(main())

'''
fetching the data

5secs

Data fetched!
Data: API data
Sending data to Lebron.....
Sending data to Jordan.....

5secs

Data sent to Lebron!
Data sent to Jordan!
Authorisation server is up and running

5secs

Auth server received
In the auth server, Cristiano
'''
