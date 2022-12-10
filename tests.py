import helpers as h

sample = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
          [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1], 
          [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0], 
          [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]]

def test_crossover(sample):
    

    for p in sample:
        print(p)
    ch = []
    ch = h.crossover(sample)
    print()
    for c in ch:
        print(c)


def test_mutation(sample):
    for p in sample:
        print(p)
    
    ch = []
    ch = h.mutate(sample)
    print()
    for c in ch:
        print(c)


if __name__ == "__main__":
    test_mutation(sample)