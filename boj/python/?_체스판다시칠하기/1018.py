'''
하나씩 탐색을 하다가
N-i값이 먼저 8이 되면 그 지점을 기준으로, 더이상 내려가지 않고 오른쪽으로만 탐색
M-i값이 먼저 8이 되면, 그 지점을 기준으로 더이상 오른쪽으로 가지 않고 내려가면서만 탐색
두 값 모두 8이 되면 그 지점을 선택
탐색은 밑의 변과 옆의 변이 다른 색일 경우
'''
N, M = map(int, input().split()) # NxM의 판때기

plat = []

for _ in range(N):
    plat.append(list(input()))

start_point = plat[0][0]

for i in range(N):
    if N-i

