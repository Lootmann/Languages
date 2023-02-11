import asyncio


async def sleepin(idx: float, sec: float = 0.2):
    await asyncio.sleep(sec)
    print(idx)


async def main():
    for i in range(10):
        print("start ", i)
        await sleepin(i)


if __name__ == "__main__":
    asyncio.run(main())
