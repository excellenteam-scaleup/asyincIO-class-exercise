import asyncio
from datetime import datetime
# Enables us to run syinc functions with an event loop



async def sleep(seconds: int) -> None:
# This is an asyinc function definition - returns a coroutine
    print(f"Sleeping for {seconds} seconds...")
    print(datetime.now())
    # Delegate IO to OS and give control back to the event loop
    await asyncio.sleep(seconds)
    print(f"Woke up after {seconds} seconds!")

async def main():
    # Receives multiple coroutines, generates tasks out of them and executes them
    # await asyncio.gather(sleep(2), sleep(2))
    await asyncio.gather(sleep(1), sleep(3), sleep(2))
    # await sleep(3)
    # await sleep(1)
    # await sleep(2)

import time

def regular_sleep(seconds):
    print(f"Regular sleeping for {seconds} seconds...")
    time.sleep(seconds)
    print(f"Regular woke up after {seconds} seconds!")


def regular_main():
    for _ in range(2):
        regular_sleep(2)

if __name__ == '__main__':
    # Starts the actual event loop
    asyncio.run(main())
    # regular_main()
    a = sleep(2)
    print()

