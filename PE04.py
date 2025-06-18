#horrible awful no good n^2
#906609
import math 

def isPalindrome(n): 
  n = str(n)
  for i in range(math.floor(len(n)/2)):
    if n[i] != n[len(n)-i-1]: 
      return False
  return True

largest = 0
for i in range (999, 99, -1):
  for j in range(999, 99, -1):
    if isPalindrome(i*j) and i*j > largest:
      largest = i*j

print(largest)