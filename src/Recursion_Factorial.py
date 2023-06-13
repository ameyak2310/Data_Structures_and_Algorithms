"""
Calculates Factorial Recursively
"""
import time

#%% Function


def factorial_recur(number):
    """Calculate facorial of an interger recursively
    Args:
        n (int): Integer
    Returns:
        result: returns factorial of Interger n
    """
    if number == 0:
        result = 1
    elif number == 1:
        result = 1
    else:
        result = number*factorial_recur(number-1)
    return result

#%% Function Call

NUMBER = 10
func = factorial_recur

print("\n___OUTPUT with Recursion___")
start_time = time.time()
print(f"Factorial of {NUMBER} : {func(NUMBER)}")
end_time = time.time()
print(f"Compute time : {end_time-start_time}\n")

