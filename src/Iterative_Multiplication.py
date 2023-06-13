""" 
Iterative multiplication of two number
"""
import time

#%% Function


def multiply(a,b):
    """Multiples two integers without recursion
    Args:
        a (_int_): First integer
        b (_int_): Second integer
    """
    result = 0
    while b > 0:
        result = result + a
        b = b - 1   
    return result


#%% Function call


Num_1,Num_2 = 4826781678,500
func = multiply

print("\n___OUTPUT without Recursion___\n")
start_time = time.time()
print(f"Product of {Num_1} x {Num_2}: {func(Num_1,Num_2)}")
end_time = time.time()
print(f"Compute time : {end_time-start_time}\n")