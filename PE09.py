# find abc s.t. a^2 + b^2 = c^2, a + b + c = 1000
# a < b < c

# 31875000
flag = False
for c in range (333, 1000 - 3 + 1): 
    for b in range (1, 1000 + 1 - c):
        a = (c**2 - b**2)**0.5
        print("A: ", a, " b: ", b, " c: ", c)
        if (a + b + c == 1000):
            flag = True
            print(a*b*c)
            break
    if (flag):
        break

