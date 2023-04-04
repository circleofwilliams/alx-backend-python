#!/usr/bin/env python3
''' Yield a random number with an asynchronous functions (coroutine)
'''
import random, typing, asyncio


async def async_generator() -> typing.Generator[float, None, None]:
    ''' The coroutine to yield a random number and sleep 1s
    '''
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
