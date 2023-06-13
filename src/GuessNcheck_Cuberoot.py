#%%Guess and Check Algorithm
"""
Demonstration of the Guess and check Algorithm
Ref: MIT 6.001 (2016) Lecture 3
"""
import time

NUM = int(input('\nEnter number to find cuberoot:\n'))

start_time = time.time()

for guess in range(abs(NUM)+1):
    if guess**3 >= abs(NUM):
        break

if guess**3 == abs(NUM):
    if NUM < 0:
        guess = -guess
        print(f"\nCube root of {NUM} is {guess}")
    else:
        print(f"\nCube root of {NUM} is {guess}")
else:
    print(f"\nNumber {NUM} is not a perfect cube !")

end_time = time.time()
print(f"Time to compute : {end_time - start_time} seconds\n")
# %%
