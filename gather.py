import asyncio
async def count_till_num(num):
    print("The process started")
    await asyncio.sleep(2)
    print('process finished!')

async def main():
    print("gather function started")
    list_of_functions = []
    for i in range(1,1001):
        list_of_functions.append(count_till_num(i))
    await asyncio.sleep(2)
    await asyncio.gather(*list_of_functions)
    print("Done!")

if __name__ == '__main__':
    asyncio.run(main())