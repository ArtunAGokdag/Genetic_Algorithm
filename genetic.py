import random
import numpy as np
import helpers as h

N_POP = 6
N_CHILD = 4
GENERATIONS = 3
SATISFACTION = 6

def ga():

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