# longest collatz sequence from a starting term under one mil

def get_next_term(n):
    if n % 2 == 0:
        return n/2
    else: 
        return (3*n + 1)

max_len = 1 # starting term of 1
x = 1
for i in range (3, 1000000): 
    terms = []
    next_term = get_next_term(i)
    while (next_term != 1):
        terms.append(next_term)
        next_term = get_next_term(next_term)
    if len(terms) > max_len:
        print("i: ", i, "length: ", len(terms))
        max_len = len(terms)
        x = i

print(x)
# 837799