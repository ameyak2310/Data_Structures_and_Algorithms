import time
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(15000000)
print(sys.getrecursionlimit())

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

Num_1,Num_2 = 4826781678,500


print("\n___OUTPUT without Recursion___\n")
start_time = time.time()
print(f"Product of {Num_1} x {Num_2}: {multiply(Num_1,Num_2)}")
end_time = time.time()
print(f"Compute time : {end_time-start_time}\n")

print("\n___OUTPUT with Recursion___\n")
start_time = time.time()
print(f"Product of {Num_1} x {Num_2}: {multiply_recursively(Num_1,Num_2)}")
end_time = time.time()
print(f"Compute time : {end_time-start_time}\n")
