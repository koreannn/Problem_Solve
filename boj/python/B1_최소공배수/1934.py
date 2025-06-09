"""
- 최소공배수 = a*b // 최대공약수
- 최대공약수 구하는 방식: a,b = b, a%b 반복(b=0)일때까지

"""

t = int(input())
answer = []

def gdc(a, b): # 최대공약수
    while b!= 0:
        a, b = b, a%b # 10,24 => 24, 10 -> 10, 4 -> 4, 2 -> 2, 0
    return a

def lmc(a, b): # 최소공배수
    num = a*b // gdc(a, b)
    return num

for _ in range(t):
    a, b = map(int, input().split())
    answer.append(str(lmc(a, b)))

print('\n'.join(answer))

