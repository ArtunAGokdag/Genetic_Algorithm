import random
import helpers
from helpers import BIT_LENGTH, decode, fitness
N_POP = 6
GENERATIONS = 100

def ga():

    soultions = [] # contains both x and y in 16 bit binary list
    s = [] # used for iteration
    # Populate gen 1 random
    for _ in range(N_POP):
        for _ in range(BIT_LENGTH):
            s.append(random.randint(0,1))
        
        soultions.append(s)
        s = []
    

    # Encode

    # Evaluate
    ranked_solutions = []   # fitness value, chrm
    for s in soultions:
        print (decode(s), s)
        ranked_solutions.append(( fitness(decode(s)), s))

    print()
    ranked_solutions.sort(reverse=True)
    for r in ranked_solutions:
        print(r)

    # Select Parents

    # Cross over

    # Mutate

ga()