from math import sqrt

t = int(input())
answer = []

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    if (x1 == x2) and (y1 == y2) and (r1 == r2): # 두 원이 정확히 일치할 경우
        answer.append("-1")
    elif sqrt((x1-x2)**2 + (y1-y2)**2) == float(r1 + r2) or sqrt((x1-x2)**2 + (y1-y2)**2) == float(abs(r1 - r2)): # 접함(외접하거나, 내접하거나)
        answer.append("1")
    elif float(abs(r1-r2)) < sqrt((x1-x2)**2 + (y1-y2)**2) < float(r1 + r2): # 두 점에서 만날 경우 
        answer.append("2")
    else:
        answer.append("0")
    
print('\n'.join(answer))