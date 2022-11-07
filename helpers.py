from math import exp
import random


BIT_LENGTH = 16
CROSSOVER_PROB = 0.7
MUTATION_PROB = 0.0001
upper_bound = 3
lower_bound = -3
SENSITIVITY = (upper_bound - lower_bound ) / ((2**(BIT_LENGTH//2)) - 1)

#objective function
def objective(x , y):
    return(((1-x)**2 * exp((-x**2) - (y+1)**2)) - ((x - x**3 - y**5) * exp(-x**2 - y**2)))

#evaluate fitness
def fitness(points):
    return (objective(points[0], points[1])) ** 3

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
    x_b = chrm[:BIT_LENGTH // 2]
    y_b = chrm[BIT_LENGTH // 2:]

    # Convert to int
    x,y, i = 0,0,0
    for bit in reversed(x_b):
        x += bit *( 2 ** i)
        i+=1
    
    i = 0
    for bit in reversed(y_b):
        y += bit * (2 ** i)
        i+=1
    
    # Map to function range
    x = x * SENSITIVITY - upper_bound;
    y = y * SENSITIVITY - upper_bound;

    return (x,y)
    

#TODO:
def Mutate():
    pass

#TODO:
def Crossover():
    pass



