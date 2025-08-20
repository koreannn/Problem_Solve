"""
프로그래머스 문제 X, 현대오토에버 2024 신입채용 문제

- 보급품 -> 각 팀마다 챙기기 (N: 보급품의 개수)
- 팀에는 신입 사원 k명이 존재
- 보급품은 무게와 가치가 정해져있음. 각각의 보급품은 유일함(하나만 존재)
- 사원 한 명이 담을 수 있는 최대 무게: M, 가방은 사원당 딱 한 개씩만


최대 무게를 초과하지 않게 각자 가방에 보급품을 담을 때, 가치가 최대가 되도록

e.g.
5 2 5 -> 각각 N, K, M
4 5 -> 보급품의 무게, 보급품의 가치
3 4
2 1
5 7
1 1

답: 13
두 명중 한명이 (5, 7)을 가져가고, 다른 한 명이 (4,5)와 (1,1)을 가져가면 총 합 13
"""

N, K, M  = map(int, input().split())
supplies = []
answer = 0 # 보급품 가치의 총 합

for _ in range(N):
    weight, value = map(int, input().split())
    supplies.append([weight, value])

sorted_supplies = sorted(supplies, key=lambda x: x[1], reverse=True)

# 아예 못넣는 보급품일 경우 제거
filtered_supplies = list(filter(lambda x: x[0] <= M, sorted_supplies))


curr = M
start_index = 0
while K > 0:
    for i in range(start_index, len(filtered_supplies)):
        if curr == 0:
            K -= 1
            curr = M
            start_index = i
            break
    
        answer += filtered_supplies[i][1]
        curr -= filtered_supplies[i][0]

print(answer)
