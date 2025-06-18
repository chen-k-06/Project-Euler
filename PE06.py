sum = 0
sqed_sum = 0
for i in range(101):
    sum += i
    sqed_sum += i**2
print(sum**2 - sqed_sum) #25164150