from threading_module import task, thread_maker
import time

def worker(times_list, index):
    start_time = time.thread_time()
    task()
    end_time = time.thread_time()
    times_list[index] = end_time - start_time
    
def measure_times(num_threads):
    times_list = [0] * num_threads

    process_start = time.process_time()
    thread_maker(num_threads, times_list, worker)
    process_end = time.process_time()

    process_time_elapsed = process_end - process_start
    return times_list, process_time_elapsed