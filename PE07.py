import math 
primes = [0] * 10001
primes[0] = 2
num = 3
i = 1

def isPrime(n):
  if n % 2 == 0:
      return False
  for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
      if n % i == 0:
          return False
  return True

while(True):
  if (isPrime(num)):
    primes[i] = num
    print("prime: ", primes[i], " at i ", i)
    if i == 10000:
      break
    i += 1
  num += 1

print(primes[10000]) # 104743