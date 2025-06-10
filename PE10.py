# sum of all primes below 2000000
import math
def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range (3, math.floor(n**(0.5)) + 1):
        if n % i == 0:
            return False
    return True
sum = 17
for i in range (11, 2000001, 2):
    if isPrime(i):
        sum += i

print(sum)
# 142913828922