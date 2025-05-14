   

# for linux
# import os
# import time

# def process_demo():
#     pid = os.fork()
#     if pid > 0:
#         print("Parent process waiting...")
#         os.wait()
#         print("Parent finished.")
#     elif pid == 0:
#         print("Child process running...")
#         time.sleep(2)
#         print("Child done.")

# process_demo()






# for windows

from multiprocessing import Process
import time
import os

def child():
    print(f"Child Process ID: {os.getpid()}")
    print("Child process running...")
    time.sleep(2)
    print("Child process finished.")

def process_demo():
    print(f"Parent Process ID: {os.getpid()}")
    p = Process(target=child)
    p.start()             # Start the child process (like fork)
    print("Parent process waiting for child to finish...")
    p.join()              # Wait for child process to complete (like wait)
    print("Parent process finished.")

if __name__ == "__main__":
    process_demo()
