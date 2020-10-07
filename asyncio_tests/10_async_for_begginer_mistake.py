import asyncio


class AsyncIterator:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __aiter__(self):
        return self

    async def __anext__(self):
        print(f'start {self.i}')
        await asyncio.sleep(1)
        print(f'end {self.i}')
        if self.i >= self.n:
            raise StopAsyncIteration
        self.i += 1
        return self.i


async def main():
    async for i in AsyncIterator(10):
        print(f'finally {i}')


if __name__ == '__main__':
    asyncio.run(main())

# start 0
# start 1
# ... start 10

# end 0
# end 1
# ... end 10

# finally 0
# finally 1
# ... finally 10
