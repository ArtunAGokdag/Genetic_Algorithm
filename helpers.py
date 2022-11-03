from math import exp
import random
import bitstring

N_POP = 6
BIT_LENGTH = 8
CROSSOVER_PROB = 0.7
MUTATION_PROB = 0.0001
upper_bound = 3
lower_bound = -3
SENSITIVITY = (upper_bound - lower_bound ) / ((2**BIT_LENGTH) - 1)

#objective function
def objective(x , y):
    return(((1-x)**2 * exp((-x**2) - (y+1)**2)) - ((x - x**3 - y**5) * exp(-x**2 - y**2)))

#evaluate fitness
def fitness(x, y):
    return (objective(x, y)) ** 3

#turn int to binary array
def encode(x, y):
    if x > upper_bound or x < lower_bound:
        x = x * SENSITIVITY - upper_bound
    if y > upper_bound or y < lower_bound:
        y = y * SENSITIVITY - upper_bound

    x_b = bitstring.BitArray(float=x, length=32)
    y_b = bitstring.BitArray(float=y, length=32)
    
    
    return x_b, y_b

def decode(chrm):
    
    chrm_x = chrm[:chrm.len//2]
    chrm_y = chrm[chrm.len//2:]

    return chrm.int, chrm.int
    

#TODO:
def Mutate():
    pass

#TODO:
def Crossover():
    pass


encx, ency = encode(0.323945842, -1.86000000000)
print(encx.float, ency.float)

