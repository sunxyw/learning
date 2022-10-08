async def sum(a, b):
    return a + b


async def main():
    print(await sum(1, 2))


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
