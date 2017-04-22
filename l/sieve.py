def sieve(limit):
    primes = [x for x in range(2, limit+1)]

    for i in range(0, len(primes) / 2):
        if primes[i] is None:
            continue
        make_null = primes[i] + i
        while make_null < len(primes):
            primes[make_null] = None
            make_null += primes[i]

    return [x for x in primes if x is not None]


if __name__ == '__main__':
    print sieve(775147)
