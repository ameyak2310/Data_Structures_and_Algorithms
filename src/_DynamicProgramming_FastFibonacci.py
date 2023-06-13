""" 
Return Fibonnaci sequence of number
"""

def fastFibonacci(n):
    fibdict = {0:1, 1:1,}
    if n == 0 or n == 1:
        result = 1
    else:
        result = fastFibonacci(n-1) + fastFibonacci(n-1)
    return result    
    
