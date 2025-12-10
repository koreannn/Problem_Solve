N, M = map(int, input().split()) # 정점 개수, 간선 개수
graph = {node: [] for node in range(1, N + 1)}
answer = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = {node: False for node in range(1, N + 1)}

def dfs(curr_node):
    visited[curr_node] = True
    
    for next_node in graph[curr_node]:
        if not visited[next_node]: # 방문하지 않았을 경우만
            dfs(next_node)

for node in range(1, N + 1):
    if not visited[node]:
        dfs(node)
        answer += 1
        
print(answer)