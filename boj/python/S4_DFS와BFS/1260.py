from collections import deque

N, M, V = map(int, input().split()) # 정점 개수, 간선 개수, 시작 정점 번호
# graph = {}
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # if a not in graph:
    #     graph[a] = []
    # graph[a].append(b)
    
    # if b not in graph:
    #     graph[b] = []
    # graph[b].append(a)

for node in graph:
    graph[node].sort()

# DFS 탐색 과정
stack = [V] # 시작점
visited = set() # 방문했던 노드인지 확인할 때, 시간 복잡도를 낮추기 위해 set으로~
DFS_result = []
while stack:
    node = stack.pop()
    if node not in visited: 
        visited.add(node) # stack -> visited
        DFS_result.append(node)
        
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

# BFS 탐색 과정
queue = deque([V])
visited = set()
BFS_result = []
while queue:
    node = queue.popleft()
    if node not in visited:
        visited.add(node)
        BFS_result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

print(' '.join(map(str, DFS_result)))
print(' '.join(map(str, BFS_result)))