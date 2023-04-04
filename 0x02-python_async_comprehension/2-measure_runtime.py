#!/usr/bin/env python3
'''expressing coroutine using asyncio and time module
'''
import asyncio
import time
import random
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''The coroutine collect total runtime and return it
    '''
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    return time.time() - start_time
