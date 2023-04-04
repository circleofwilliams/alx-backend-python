#!/usr/bin/env python3
'''expressing coroutine using asyncio and random modules
'''
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    '''The coroutine loops and yields
    '''
    i = 0
    while(i < 10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
        i += 1
