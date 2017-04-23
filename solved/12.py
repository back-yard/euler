# https://projecteuler.net/problem=12

from l import triangle

for t in triangle.triangle(1000000):
    divisors = len(reduce(list.__add__, ([i, t//i] for i in range(1, int(t**0.5) + 1) if t % i == 0)))
    if divisors >= 500:
        print t, divisors
        break

