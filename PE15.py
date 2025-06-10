# in a 20 x 20 grid, how many paths, moving only right and down 
# given 20 spaces, choose which are right and which are left 
# you must have 10 rights and 10 downs. Just pick their positions 

def factorial(n):
    product = 1
    for i in range (2, n + 1):
        product *= i
    return product

twen = factorial(20)
forty = factorial(40)
print(forty/(twen*twen)) # 20 choose 10
# 137846528820