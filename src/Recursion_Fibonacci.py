"""
Function to return Fibonacci Series
"""
#%% Last fibonacci Element


def fib(num):
    """Return Fibonacci of an interger n
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


#%% Function call return number
NUM = 10
print("\n******************************")
for NUM in range(NUM):
    print(f"Fibonacci of {NUM} is {fib(NUM)}")
print("\n******************************")

#%% Returns Fibonacci series

def fib_series(num):
    """Returns fibonacci list of n element

    Args:
        n (int): fibonacci list of len(n) will be generated

    Returns:
        fib_list(list): Fibonacci List
    """
    fib_list = [0] + [1] * num
    for i in range(3, num + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]

    return fib_list


#%% Function call : Return List
PAYLOAD = 10
func = fib_series

print("\n******************************")
print(f"Sorted List = {func(PAYLOAD)}")
print("******************************\n")
# %%
