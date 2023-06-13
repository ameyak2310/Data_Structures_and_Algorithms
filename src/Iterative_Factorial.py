"""
Calculates Factorial Iteratively
"""
import time
#%% Function
def factorial_iter(number):
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
        result = 1
        for i in range(1,number+1):
            result = result * i
    return result
#%% Fucntion Call
NUMBER = 10
func = factorial_iter

print("\n___OUTPUT without Recursion___")
start_time = time.time()
print(f"Factorial of {NUMBER} : {func(NUMBER)}")
end_time = time.time()
print(f"Compute time : {end_time-start_time}\n")
# %%
