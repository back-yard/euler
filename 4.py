# https://projecteuler.net/problem=4

print sorted([a*b if str(a*b) == str(a*b)[::-1] else None for a in range(100, 1000) for b in range(100, 1000)], reverse=True)[0]

