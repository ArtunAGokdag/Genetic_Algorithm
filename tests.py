import helpers as h

def test_crossover():
    parents = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
               [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1], 
               [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0], 
               [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]]

    for p in parents:
        print(p)
    ch = []
    ch = h.crossover(parents)
    print()
    for c in ch:
        print(c)