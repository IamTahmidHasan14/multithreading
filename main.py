#MULTITHREDING
import threading
import time

def func(s):
  print(f"wait for {s} seconds")
  time.sleep(s)

time1 = time.perf_counter()
# Normal Code
# func(2)
# func(4)
# func(1)

# Same code using Threads
t2 = threading.Thread(target=func, args=[2])
t1 = threading.Thread(target=func, args=[4])
t3 = threading.Thread(target=func, args=[1])

#it will start the program while writing the code
t1.start()
t2.start()
t3.start()

# Wait until the thread terminates.
t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(f"Total time: {time2 - time1}")