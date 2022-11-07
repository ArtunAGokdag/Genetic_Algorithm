import random
import helpers
from helpers import BIT_LENGTH, decode
N_POP = 6

def ga():

    soultions = []
    s = []
    # Populate gen 1 random
    for _ in range(N_POP):
        for _ in range(BIT_LENGTH):
            s.append(random.randint(0,1))
        
        soultions.append(s)
        s = []
    

    # Encode
    print(soultions[0])
    print(decode(soultions[0]))
    # Evaluate
    # ranked_solutions = []
    # for s in soultions:
    #     ranked_solutions.append(( fitness(s[0],s[1]), s))

    # ranked_solutions.sort()
    # #for r in ranked_solutions:
        #print(r)

    # Select Parents

    # Cross over

    # Mutate

ga()