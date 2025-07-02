from math import lcm

# def lcm(a, b):
#     return (a*b) // gcd(a, b)
    
t = int(input())
answer = []

for _ in range(t):
    a, b = map(int, input().split())
    curr = lcm(a, b)
    answer.append(str(curr))
    
print('\n'.join(answer))
