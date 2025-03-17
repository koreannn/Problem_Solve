"""
점화식: floor[0][1]: 0층 2호에 사는 사람의 수
k=1, n=3
"""

T = int(input())
answer = []

for _ in range(T):
    k = int(input()) # 층수
    n = int(input()) # 호수
    people = []
    people.append([i for i in range(1, n+1)]) # 0층 채우기 (k=0)

    for i in range(1, k+1): # 1층부터 채우기 (k >= 1)
        floor = []
        for j in range(n): # 호수
            floor.append(sum(people[-1][:j+1])) # 바로 아랫집(아래층 같은호수)까지
        people.append(floor)
    
    answer.append(people[k][n-1])

for ans in answer:
    print(ans)