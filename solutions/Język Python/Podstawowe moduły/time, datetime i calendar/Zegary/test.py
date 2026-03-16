import time

print(time.clock_getres(time.CLOCK_MONOTONIC))
print(time.clock_gettime(time.CLOCK_MONOTONIC))

print(time.clock_getres(time.CLOCK_MONOTONIC_RAW))
print(time.clock_gettime(time.CLOCK_MONOTONIC_RAW))

print(time.clock_gettime(time.CLOCK_BOOTTIME))

print(time.clock_getres(time.CLOCK_PROCESS_CPUTIME_ID))
print(time.clock_gettime(time.CLOCK_PROCESS_CPUTIME_ID))

print(time.clock_getres(time.CLOCK_THREAD_CPUTIME_ID))
print(time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID))

print(time.clock_getres(time.CLOCK_REALTIME))
print(time.clock_gettime(time.CLOCK_REALTIME))

print(time.clock_getres(time.CLOCK_TAI))
print(time.clock_gettime(time.CLOCK_TAI))