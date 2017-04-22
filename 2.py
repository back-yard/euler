# https://projecteuler.net/problem=2

a, b, res = 1, 2, 0

while b <= 4000000:
  res += b if b % 2 == 0 else 0
  a, b = b, a + b

print res

