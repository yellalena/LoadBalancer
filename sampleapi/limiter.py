import asyncio, aiohttp
from time import time, sleep

queue = asyncio.Queue()
responses = []
routine_counters = []

def say_hello(url):
    queue.put_nowait(url)

async def send_requests(queue):
    counter = 0
    async with aiohttp.ClientSession() as session:
        while not queue.empty():
            url = await queue.get()
            if counter == 5:
                sleep(1)
                counter = 0
            resp = await session.get(url)
            async with resp:
                responses.append(resp.status)
                counter+=1


def write_image(data):
    filename = f"file-{int(time()*1000)}.jpg"
    with open(filename, "wb") as f:
        f.write(data)


async def perform_routine():
    counter = 0
    while True:
        counter += 1
        await asyncio.sleep(1)
        yield counter
        if queue.empty():
            break


async def main():
    tasks = []
    for i in range(20):
        say_hello('http://localhost:8000/api/hello/')
    tasks.append(asyncio.create_task(send_requests(queue)))
    async for i in perform_routine():
        routine_counters.append(i)
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    finally:
        assert all(x == 200 for x in responses), "something went wrong and you got blocked"
        print("all 200 OK")
        assert routine_counters, "something went wrong and routing counters weren't increasing"
        print(f"len of rountine_counters is {len(routine_counters)}")