#!/usr/bin/env python3
'''Create a measure_time function with integers n and max_delay as argument.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Use the time module to measure an approximate elapsed time.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
