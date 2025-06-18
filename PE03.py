# O(n^2)
import math
x = 600851475143
largest = 1

def isPrime(n):
  if n % 2 == 0:
      return False
  for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
      if n % i == 0:
          return False
  return True
    
if (isPrime(x)):
    print(x)
else:    
    for i in range(3, math.ceil(math.sqrt(x)) + 1, 2):
        #print(i)
        if x % i == 0:
            if (isPrime(i)): 
                largest = i
print(largest)