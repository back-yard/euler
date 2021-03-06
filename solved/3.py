# https://projecteuler.net/problem=3

import math

from l import sieve

NUM = 600851475143

primes = reversed(sieve.sieve(int(math.sqrt(NUM))))

for p in primes:
    if NUM % p == 0:
        print p
        break
