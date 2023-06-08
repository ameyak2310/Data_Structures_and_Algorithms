#%% Approximation Algorithm
"""
Demonstration of the Bisection Search Algorithm
Ref: MIT 6.001 (2016) Lecture 3
"""

import time
NUM = int(input('\nEnter a number to find the cube root:\n'))
RES = float(input('Enter a residual value for accuracy:\n'))
start_time = time.time()

NO_OF_GUESSES = 1
HIGH = abs(NUM)
LOW = 0
GUESS = 0.5*(HIGH + LOW)

while RES < abs(GUESS**3 - abs(NUM)):
    if GUESS**3 < abs(NUM):
        LOW = GUESS
    else:
        HIGH = GUESS
    print(f"Guess no {NO_OF_GUESSES}, Low = {LOW}, High={HIGH}")
    GUESS = 0.5*(HIGH + LOW)
    NO_OF_GUESSES = NO_OF_GUESSES + 1

if NUM < 0:
    GUESS = -GUESS
    print(f"\nCube root of {NUM} is {GUESS}")
else:
    print(f"\nCube root of {NUM} is {GUESS}")


end_time = time.time()
print(f"Number of guesses : {NO_OF_GUESSES}")
print(f"Time to compute : {end_time - start_time} seconds\n")
