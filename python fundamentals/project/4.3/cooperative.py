import asyncio
import time

async def count(start_time,start, end):

    for i in range(start, end + 1):
        print(i)
        await asyncio.sleep(0.1)  # Simulate some asynchronous work
    elapsed_time = time.time() - start_time
    print(f"Task for range {start}-{end} completed in {elapsed_time:.2f} seconds.")

async def main():
    start_time = time.time()
    # Create two tasks for counting
    task1 = asyncio.create_task(count(start_time,1, 50))
    task2 = asyncio.create_task(count(start_time,51, 100))

    # Wait for both tasks to complete
    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    asyncio.run(main())
