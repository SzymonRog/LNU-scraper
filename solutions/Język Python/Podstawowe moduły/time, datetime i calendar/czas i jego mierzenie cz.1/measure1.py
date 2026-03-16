import time
from very_important_lib import very_important_func

start = time.perf_counter()
very_important_func()
end = time.perf_counter()

execution_time = end - start
print(execution_time)