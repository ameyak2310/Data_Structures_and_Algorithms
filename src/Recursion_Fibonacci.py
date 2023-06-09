""" 
Return Fibonacci
1, 2, 3, 4, 5,
0, 1, 1, 2, 3, 5, 
"""

def fib(n):
    """Return Fibonacci of an interger n

    Args:
        n (int): input 

    Returns:
        result(int): Fibonacci of n
    """
    if n == 0 or n == 1:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

NUM = 100
print("\n___OUTPUT___")
for NUM in range(NUM):
    print(f'Fibonacci of {NUM} is {fib(NUM)}')