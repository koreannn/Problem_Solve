node = int(input())
edge = int(input())
graph = {i: [] for i in range(1, node+1)} # e.g. node = 7 -> 1 ~ 7번 컴퓨터
answer = 0

for i in range(edge):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1) # 무방향 그래프

visited = set()

visited.add(1)
for n in graph[1]: # 1번 컴퓨터와 연결된것들
    if n not in visited:
        

