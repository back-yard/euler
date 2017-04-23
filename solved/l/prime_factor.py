import sieve


def prime_factors(number):
    primes = sieve.sieve(number)

    factors = []

    for prime in primes:
        if number in primes and number not in factors:
            factors.append(number)
            break
        if number % prime == 0:
            factors.append(prime)
            while number % prime == 0:
                number = number/prime
    return factors

if __name__ == '__main__':
    print prime_factors(2405060)
