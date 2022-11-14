import random
import numpy as np
import helpers as h

N_POP = 6
N_CHILD = 4
GENERATIONS = 3
SATISFACTION = 6

def ga():
    '''
    # Populate gen 1 random
    solutions = np.random.randint(0,2, (N_POP,h.BIT_LENGTH)) # contains both x and y in 16 bit binary list

    print(solutions)
    

    # Evaluate
    # TODO: START LOOP
    ranked_solutions = np.ndarray(shape=(N_POP,2), dtype=object)   # fitness value, chrm
    print("== Solution Points ==")
    for s  in solutions:
        print (h.decode(s))
        np.append(ranked_solutions, ( h.fitness(h.decode(s)), s))


    print("\n== Ranked Values ==")
    #ranked_solutions.sort(reverse=True)
    for r in ranked_solutions:
        print(r)

    #Check satifaction
    if ranked_solutions[0][0] > SATISFACTION:
        #break
        pass

    # # Select Parents
    # # Cross over
    # chromosomes = []
    # for s in ranked_solutions:
    #     chromosomes.append(s[1])
    
    # for i in chromosomes:
    #     print(i[:8])
    # print()
    # chromosomes = h.crossover(chromosomes)
    
    # for i in chromosomes:
    #     print(i[:8])

    
    
    # for r in ranked_solutions:
    #     print(r[1])
    # Mutate
    '''

    # Create initial population
    pop = [np.random.randint(0, 2, h.BIT_LENGTH).tolist() for _ in range(N_POP)]
    

    for _ in range(GENERATIONS):
        # Get solution points
        ranked_solutions = []
        print("== Solution Points ==") # DEBUG
        for s in pop:
            print (h.decode(s))
            ranked_solutions.append((h.fitness(h.decode(s)) , s))
        
        print()
        # Sort
        ranked_solutions.sort(reverse=True)
        ranked_solutions = ranked_solutions[:N_POP]

        print("\n== Ranked Values ==")
        for r in ranked_solutions:
            print(r)

        print()
        # Select parents
        parents = [ranked_solutions[i][1] for i in range(N_CHILD)]
        
        # Crossover
        children = []
        children = h.crossover(parents)
        print("\nCHILDS\n", children)
        # append children
        pop = parents + children
        print("\nNew POP \n", pop)
    

ga()