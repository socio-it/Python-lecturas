from threading import Thread, Lock, Event
from multiprocessing import Process, freeze_support, set_start_method
from functools import lru_cache
import asyncio, time

# ---------- threading ----------
lock = Lock()
slow_done = Event()

def slow_thread():
    with lock: print("[thread] start slow", flush=True)
    time.sleep(3)
    with lock: print("[thread] end slow", flush=True)
    slow_done.set()

@lru_cache(maxsize=None)
def fast_thread(x: int) -> int:
    slow_done.wait()
    if x <= 1:
        return 1
    time.sleep(0.2)
    with lock: print(f"[thread] step {x}", flush=True)
    return fast_thread(x-1) + x

def run_threading():
    fast_thread.cache_clear()
    t1 = Thread(target=fast_thread, args=(12,))
    t2 = Thread(target=slow_thread)
    t1.start(); t2.start()
    t2.join();  t1.join()
    print("[thread] main done", flush=True)

# ---------- multiprocessing ----------
def slow_proc():
    print("[proc] start slow", flush=True)
    time.sleep(3)
    print("[proc] end slow", flush=True)

@lru_cache(maxsize=None)
def fast_proc(x: int) -> int:
    if x <= 1:
        return 1
    time.sleep(0.2)
    print(f"[proc] step {x}", flush=True)
    return fast_proc(x-1) + x

def run_multiprocessing():
    # cada proceso tiene su propia caché
    p1 = Process(target=fast_proc, args=(12,), name="fast")
    p2 = Process(target=slow_proc, name="slow")
    p1.start(); p2.start()
    p2.join();  p1.join()
    print("[proc] main done", flush=True)

# ---------- asyncio ----------
async def slow_async():
    print("[async] start slow")
    await asyncio.sleep(3)
    print("[async] end slow")

@lru_cache(maxsize=None)
def fast_sync(x: int) -> int:  # bloquea el loop si lo llamas directo
    if x <= 1:
        return 1
    time.sleep(0.2)
    print(f"[async-blocking] step {x}")
    return fast_sync(x-1) + x

async def run_asyncio():
    await slow_async()
    # si quieres correr código CPU/sincrono, mándalo a un hilo:
    res = await asyncio.to_thread(fast_sync, 12)
    print("[async] done", res)

if __name__ == "__main__":
    freeze_support()
    try: set_start_method("spawn")
    except RuntimeError: pass

    run_threading()         # no hay ejecuciones en nivel superior
    run_multiprocessing()   # sin duplicados
    asyncio.run(run_asyncio())
