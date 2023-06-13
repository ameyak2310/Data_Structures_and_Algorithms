""" 
Function to recursively multiply two numbers
"""

import time
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(15000000)
print(sys.getrecursionlimit())

#%% Fucntion

def multiply_recursively(a,b):
    """Multiples two integers with recursion
    Args:
        a (_int_): First integer
        b (_int_): Second integer
    """
    result = 0
    if b == 1:
        result = a
    else:
        result =  a + multiply_recursively(a,b-1)
    return result

#%% Fuctino Call

Num_1,Num_2 = 4826781678,500

print("\n___OUTPUT with Recursion___\n")
start_time = time.time()
print(f"Product of {Num_1} x {Num_2}: {multiply_recursively(Num_1,Num_2)}")
end_time = time.time()
print(f"Compute time : {end_time-start_time}\n")
