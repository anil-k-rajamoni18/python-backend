from itertools import permutations

data = list(permutations(['A', 'B', 'C'], 3))  # [('A', 'B'), ('A', 'C'), ...]

print(data)