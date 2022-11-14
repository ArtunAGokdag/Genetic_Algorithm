import random
import helpers as h

N_POP = 6
GENERATIONS = 100
SATISFACTION = 6

def ga():

    soultions = [] # contains both x and y in 16 bit binary list
    s = [] # used for iteration
    # Populate gen 1 random
    #TODO: find a better way
    for _ in range(N_POP):
        for _ in range(h.BIT_LENGTH):
            s.append(random.randint(0,1))
        
        soultions.append(s)
        s = []
    

    # Evaluate
    ## START LOOP
    ranked_solutions = []   # fitness value, chrm
    print("== Solution Points ==")
    for s in soultions:
        print (h.decode(s))
        ranked_solutions.append(( h.fitness(h.decode(s)), s))


    print("\n== Ranked Values ==")
    ranked_solutions.sort(reverse=True)
    # for r in ranked_solutions:
    #     print(r[1][:8])

    #Check satifaction
    if ranked_solutions[0][0] > SATISFACTION:
        #break
        pass

    # Select Parents
    # Cross over
    chromosomes = []
    for s in ranked_solutions:
        chromosomes.append(s[1])
    
    for i in chromosomes:
        print(i[:8])
    print()
    chromosomes = h.crossover(chromosomes)
    
    for i in chromosomes:
        print(i[:8])

    
    
    # for r in ranked_solutions:
    #     print(r[1])
    # Mutate

ga()