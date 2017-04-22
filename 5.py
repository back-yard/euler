# https://projecteuler.net/problem=5

numbers = range(1, 21)

gcd, lcm = lambda a, b: a if b == 0 else gcd(b, a % b), lambda a, b: (a * b) / gcd(a, b)
print reduce(lcm, numbers)
