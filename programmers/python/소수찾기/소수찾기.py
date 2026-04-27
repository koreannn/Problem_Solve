import math

def solution(n):
    answer = 0
    is_prime = [True] * (n + 1)
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i ** 2, n + 1, i):
                is_prime[j] = False
    
    return answer

# test
print(solution(10)) # 4
print(solution(5)) # 3