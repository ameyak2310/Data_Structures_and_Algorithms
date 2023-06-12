""" 
Function to return Fibonacci Series
"""
#%% Last fibonacci Element


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


#%% Function call return number          
NUM = 10
print("\n___OUTPUT___")
for NUM in range(NUM):
    print(f'Fibonacci of {NUM} is {fib(NUM)}')
    
#%% Returns Fibonacci series


def fib_series(n):
    fib_list = [1] * n + [1]
    fib_list[0] = 0
    for i in range(3, n+1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
        
    return fib_list
       

#%% Function call : Return List
PAYLOAD = 10
func = fib_series

print("\n******************************")
print(f"Sorted List = {func(PAYLOAD)}")
print("******************************\n")
# %%
