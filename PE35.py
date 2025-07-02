from get_primes_function import isPrime

def get_rotations(n):
    '''n is an integer between 0 and 10000'''
    original_n = n
    my_list = []
    str_n = str(n)
    num_digits = len(str_n)
    multiplier = 10**(num_digits-1)
    my_list.append(n)

    while True: 
        n = (n % 10)*multiplier + n//10
        my_list.append(n)
        if (n == original_n):
            break

    return list(set(my_list))

if __name__ == "__main__":
    prime_count = 13 # under 100
    flag = False
    primes = []

    for i in range(101, 1000001):
        if (i %2 == 0 or i % 3 == 0 or isPrime(i) == False):
            continue
        flag = False
        rotations = get_rotations(i)
        for num in rotations: 
            if (isPrime(num) == False):
                flag = True
                break
        if (flag == False):
            print(rotations)
            prime_count += 1
            primes.append(i)

    print(prime_count)
    print(len(primes) + 13) # 55 
    # make sure to include 13 and 31 -> this counts as 2, NOT 1


