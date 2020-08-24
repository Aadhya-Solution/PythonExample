# File: sys-exitfunc-example-1.py

import sys

def hello():
    print("This is world")

sys.exitfunc = hello

print("hello")
sys.exit()
print("there") # never printed