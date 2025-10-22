from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import math

def is_prime(n: int) -> bool:
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def cpu_task(span):
    # cuenta primos en un rango [base, base+span)
    base = 3_000_000
    count = 0
    for x in range(base, base + span):
        if is_prime(x):
            count += 1
    return count
def task_thread(n):
    time.sleep((n-1)/n)

def pool(x):
    with ProcessPoolExecutor(max_workers=x) as executor:
        start =time.perf_counter()
        list(executor.map(cpu_task, range(100,200,1)))
        end =time.perf_counter()
        print(f"el tiempo es :{end-start}")
    with ThreadPoolExecutor(max_workers=x) as executor:
        start =time.perf_counter()
        list(executor.map(task_thread, range(100,130,1)))
        end =time.perf_counter()
        print(f"el tiempo es :{end-start}")

def pool_as_completed(x):
    with ProcessPoolExecutor(max_workers=x) as executor:
        start =time.perf_counter()
        [executor.submit(cpu_task,i) for i in  range(100,200,1) ]
        end =time.perf_counter()
        print(f"el tiempo es :{end-start}")
    with ThreadPoolExecutor(max_workers=x) as executor:
        start =time.perf_counter()
        [executor.submit(task_thread, i) for i in  range(100,200,1) ]
        end =time.perf_counter()
        print(f"el tiempo es :{end-start}")

if __name__ == "__main__":
    pool(1)
    pool(10)
    pool_as_completed(1)
    pool_as_completed(10)