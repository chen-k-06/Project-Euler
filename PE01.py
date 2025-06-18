# theta n, n = range 
def sumDivBy(n):
    sum = 0
    for i in range(1000):
        if i % n == 0:
            sum += i
    return sum
print(sumDivBy(3) + sumDivBy(5) - sumDivBy(15))

# alternatively, loop through 1000 and add to sum if divisible by 3 or 5