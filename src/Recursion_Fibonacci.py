"""
Function to return Fibonacci Series
"""
#%% Last fibonacci Element


def fib(num):
    """Returns Fibonacci of an interger n
    Args:
        n (int): input
    Returns:
        result(int): Fibonacci of n
    """
    if num in (0,1):
        result = 1
    else:
        result = fib(num - 1) + fib(num - 2)
    return result


#%% Function call returns number
NUM = 10
print("\n******************************")
for NUM in range(NUM):
    print(f"Fibonacci of {NUM} is {fib(NUM)}")
print("\n******************************")
