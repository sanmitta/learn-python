import random
import time
from functools import wraps

def record_time(fn):
    def timed(*args, **kwargs):
        t_start = time.time()
        result = fn(*args, **kwargs)
        t_end = time.time()
        print((t_end - t_start) * 1000000000)
        return result
    return timed

@record_time
def hello():
    print('Hello SMX')

hello()