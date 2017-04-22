# https://projecteuler.net/problem=6

print sum(range(1, 101))**2 - sum(x**2 for x in range(1, 101))
