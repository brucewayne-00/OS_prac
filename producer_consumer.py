import threading
import time
import random

buffer = []
buffer_size = 5
mutex = threading.Lock()
empty = threading.Semaphore(buffer_size)
full = threading.Semaphore(0)

# Number of items to produce and consume
TOTAL_ITEMS = 10

# Control flags
stop_event = threading.Event()

def producer():
    for _ in range(TOTAL_ITEMS):
        item = random.randint(1, 100)
        empty.acquire()
        with mutex:
            buffer.append(item)
            print(f"[Producer] Produced: {item}")
        full.release()
        time.sleep(random.uniform(0.1, 0.5))
    stop_event.set()  # Signal to stop after producing

def consumer():
    while not stop_event.is_set() or full._value > 0:
        full.acquire()
        with mutex:
            if buffer:
                item = buffer.pop(0)
                print(f"[Consumer] Consumed: {item}")
        empty.release()
        time.sleep(random.uniform(0.1, 0.5))

# Start threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Wait for threads to finish
producer_thread.join()
consumer_thread.join()

print(" Producer and Consumer have finished.")
