import helpers
from helpers import N_POP

def ga():

    soultions = []
    # Populate gen 1 random
    for _ in range(N_POP):
        soultions.append((random.uniform(-3,3),
                          random.uniform(-3,3)))  
    # Encode
    
    # Evaluate
    ranked_solutions = []
    for s in soultions:
        ranked_solutions.append(( fitness(s[0],s[1]), s))

    ranked_solutions.sort()
    #for r in ranked_solutions:
        #print(r)

    # Select Parents

    # Cross over

    # Mutate

