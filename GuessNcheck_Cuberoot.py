# Guess and Check Algorithm

num = -27

for guess in range(abs(num)+1):
    if guess**3 >= abs(num):
        break

if guess**3 == abs(num):
    if num < 0:
        guess = -guess
        print(f"\nCube root of {num} is {guess}\n")
    else:
        print(f"\nCube root of {num} is {guess}\n")    
else:
    print(f"\nNumber {num} is not a perfect cube !\n")