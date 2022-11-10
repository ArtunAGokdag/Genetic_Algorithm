import random
import helpers
from helpers import BIT_LENGTH, decode, fitness
N_POP = 6
GENERATIONS = 100
SATISFACTION = 6

def ga():

    soultions = [] # contains both x and y in 16 bit binary list
    s = [] # used for iteration
    # Populate gen 1 random
    #TODO: find a better way
    for _ in range(N_POP):
        for _ in range(BIT_LENGTH):
            s.append(random.randint(0,1))
        
        soultions.append(s)
        s = []
    

    # Evaluate
    ## START LOOP
    ranked_solutions = []   # fitness value, chrm
    print("== Solution Points ==")
    for s in soultions:
        print (decode(s))
        ranked_solutions.append(( fitness(decode(s)), s))


    print("\n== Ranked Values ==")
    ranked_solutions.sort(reverse=True)
    for r in ranked_solutions:
        print(r)

    #Check satifaction
    if ranked_solutions[0][0] > SATISFACTION:
        #break
        pass
    
    # Select Parents

    # Cross over

    # Mutate

ga()