# File: sys-setprofiler-example-1.py
'''
The setprofiler function allows you to install a profiling function. 
This is called every time a function or method is called, at every return 
(explicit or implied), and for each exception:
'''
import sys

def test(n):
    j = 0
    for i in range(n):
        j = j + i
    return n

def profiler(frame, event, arg):
    print event, frame.f_code.co_name, frame.f_lineno, "->", arg

# profiler is activated on the next call, return, or exception
sys.setprofile(profiler)

# profile this function call
test(1)

# disable profiler
sys.setprofile(None)

# don't profile this call
test(2)

## call test 3 -> None
## return test 7 -> 1
