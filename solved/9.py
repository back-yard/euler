# https://projecteuler.net/problem=9

print [i for i in set(a * b * (1000 - (a + b)) if a ** 2 + b ** 2 == (1000 - (a + b)) ** 2 else None for a in range(1000 / 3) for b in range(a + 1, 1000 / 2)) if i is not None][0]
