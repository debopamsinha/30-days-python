def is_prime(n):
    if n == 2 :
        return 'Prime'
    elif n==1 or n%2 == 0 :
        return 'Not prime'
    for i in range(3, int(n**0.5) + 1, 2):
        if n%i == 0 :
            return 'Not prime'
    return 'Prime'   
T = int(input())
for _ in range (T) :
    n = int(input())
    print(is_prime(n))