#%% Approximation Algorithm
"""
Demonstration of the Approximation Algorithm
Ref: MIT 6.001 (2016) Lecture 3
"""

import time

NUM = int(input('\nEnter a number to find the cube root:\n'))
RES = float(input('Enter a residual value for accuracy:\n'))
LR = float(input('Enter a learning rate for program:\n'))

start_time = time.time()
GUESS = 0
NO_OF_GUESSES = 0

while RES <= abs(GUESS**3 - abs(NUM)) and GUESS < abs(NUM):
    GUESS = GUESS + LR
    NO_OF_GUESSES = NO_OF_GUESSES + 1

if NUM < 0:
    GUESS = -GUESS
    print(f"\nCube root of {NUM} is {GUESS}")
else:
    print(f"\nCube root of {NUM} is {GUESS}")

end_time = time.time()
print(f"Number of guesses : {NO_OF_GUESSES}")
print(f"Time to compute : {end_time - start_time} seconds\n")
