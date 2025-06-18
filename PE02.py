#linear 
fib = [0] * 4000000
fib[0] = 1
fib[1] = 2
sum = 2
i = 2
while (True): 
    fib[i] = fib[i-1] + fib[i-2]
    if fib[i] > 4000000:
        break
    if fib[i] % 2 == 0:
        sum += fib[i]
    i += 1
print(sum)