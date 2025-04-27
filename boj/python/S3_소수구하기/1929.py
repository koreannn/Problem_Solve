m, n = map(int, input().split()) # 1<= n, m <= 1,000,000
# answer = []

# def is_prime(num: int) -> bool:
#     prime_TF = False
#     for i in range(2, num):
#         if num%i == 0:
#             return prime_TF
#     prime_TF = True
#     return prime_TF

# for num in range(m, n+1):
#     if num == 1:
#         continue
#     if is_prime(num):
#         answer.append(str(num))

def lin_sieve(n):
    is_prime = [True] * (n+1)
    primes = []
    for num in range(2, n+1):
        if is_prime[num]:
            primes.append(num)
        for p in primes:
            if num*p > n:
                break
            is_prime[num*p] = False
            if num%p == 0:
                break
    return primes

primes = lin_sieve(n)

for p in primes:
    if p >= m:
        print(p)