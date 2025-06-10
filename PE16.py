# sum of the digits of the number 2^1000
import math 
x = 2**1000
sum = 0
print(x)
while (x != 0):
    quotient, remainder = divmod(x, 10) # or use // integer division 
    sum += remainder
    x = quotient

print(sum) # 1366