# first triangle number to have over 500 divisors
import math
def count_divisors(n):
    d_count = 1; # 1 and itself
    for i in range (2, math.floor(n**0.5)):
        if n % i == 0:
            d_count += 1
    d_count *= 2
    if n % (math.floor(n**0.5)) == 0: 
        d_count += 1
    return d_count

i = 7
n = 28
while(True):
    while (n < 50000):
        i += 1
        n += i
    count = count_divisors(n)
    print("Count ", count)
    if (count > 500):
        print(n)
        break
    i += 1
    n += i

# 76576500