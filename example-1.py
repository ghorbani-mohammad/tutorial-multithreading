# Suppose we have two functions f and g.
# We want to calculate max of their output.
# You should calculate the output of those function in concurrent running.

import time
import random
from threading import Thread


def f():
    value = random.choice([1, 3, 5, 7, 9])
    print(f"value from f: {value}")
    time.sleep(value)
    return value


def g():
    value = random.choice([2, 4, 6, 8, 10])
    print(f"value from g: {value}")
    time.sleep(value)
    return value


print(max(f(), g()))


# Now lets use multithreading
threads = [Thread(target=f), Thread(target=g)]

# f and g run in separate threads
for thread in threads:
    thread.start()

# Wait until both f and g have finished
for thread in threads:
    thread.join()
# or print(max(threads[0].join(), threads[1].join()))

# At above implementation we have a limit.
# The limit is that we can't get return values from threads
# So lets implement in another way in which we can get return values from threads


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


threads = [ThreadWithReturnValue(target=f), ThreadWithReturnValue(target=g)]
# f and g run in separate threads
for thread in threads:
    thread.start()

print(max(threads[0].join(), threads[1].join()))
