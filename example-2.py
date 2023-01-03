# concurrent.futures

# Python 3.2 introduced the concurrent.futures module that provides a simpler interface
# to bring together both the threading and multiprocessing modules. It makes use of the
# ThreadPoolExecutor and ProcessPoolExecutor classes to manage thread and process pools,
# which share much of the same interface to make switching between multithreading and multiprocessing easier.
# Interface aside, the concurrent.futures module is conceptually the same as the threading and multiprocessing modules.
import time
from concurrent.futures import ThreadPoolExecutor


def io_bound_job():
    time.sleep(5)


def run_with_threads(n_jobs, sites):
    # `max_workers` specifies the max number threads to created.
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        # When the target function is mapped to a list or tuple, the target function
        # is executed for every element of the list or tuple in a separate thread.
        executor.map(io_bound_job, sites)


# Get a list of fake websites for testing.
sites = [f"https://httpbin.org/get?id={i}" for i in range(20)]

# Run with one thread:
start_one_thread = time.time()
run_with_threads(n_jobs=1, sites=sites)
duration = time.time() - start_one_thread
print(f"IO-bound job finished in {duration:.2f} seconds with one thread.")

# Run with ten threads:
start_three_threads = time.time()
run_with_threads(n_jobs=10, sites=sites)
duration = time.time() - start_three_threads
print(f"IO-bound job finished in {duration:.2f} seconds with three threads.")
