"""
Returns Fibonacci series
"""
#%% Function


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