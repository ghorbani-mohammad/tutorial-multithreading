# Suppose we have two functions f and g.
# We want to calculate max of their output.
# You should calculate the output of those function in concurrent running.

import time
import random


def f():
    time.sleep(5)
    return random.choice([1, 3, 5, 7, 9])


def g():
    time.sleep(8)
    return random.choice([2, 4, 6, 8, 10])


print(max(f(), g()))
