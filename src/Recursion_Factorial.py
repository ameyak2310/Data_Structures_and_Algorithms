def calcFactorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*calcFactorial(n-1)
    
print('Output\n')    
print(calcFactorial(5))
    