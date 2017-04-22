# https://projecteuler.net/problem=5

NUM = 20

gcd, lcm = lambda a, b: a if b == 0 else gcd(b, a % b), lambda a, b: (a * b) / gcd(a, b)
print reduce(lcm, range(1, NUM + 1))
