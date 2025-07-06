from math import sqrt

t = int(input())
answer = []

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = sqrt((x1-x2)**2 + (y1-y2)**2) # 두 점 사이의 거리
    
    if x1 == x2 and y1 == y2 and r1 == r2:
        answer.append("-1")
    elif (abs(r1-r2) == dist) or (r1+r2 == dist):
        answer.append("1")
    elif abs(r1-r2) < dist and dist < r1 + r2:
        answer.append("2")    
    else:
        answer.append("0")

print('\n'.join(answer))