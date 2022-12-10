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
        # Evaluate solution points
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
        print("PARENTS")
        for i in parents:
            print(i)
        
        children = []
        children = h.crossover(parents)
        
        # TODO: Mutate
        children = h.mutate(children)
        
        # OUTPUT
        print("\nCHILDREN\n")
        for i in children:
            print(i)

        # append children
        pop = parents + children
        print("\nNew POP \n")
        for i in pop:
            print(i)

        # TODO: get best solution to plot
        best_solution = h.decode(pop[0])
        # TODO: Decode chrm tho show points    

if __name__ == "__main__":
    ga()