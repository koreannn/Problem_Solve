from collections import deque

N, M, V = map(int, input().split()) # 정점 개수, 간선 개수, 시작 노드
dfs_answer = []
bfs_answer = []
visited_dfs = {}
visited_bfs = {}

graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    
for key in graph:
    graph[key].sort()

def dfs(curr_node):
    visited_dfs[curr_node] = True
    dfs_answer.append(str(curr_node))
    
    for next_node in graph[curr_node]:
        if next_node not in visited_dfs:
            dfs(next_node)
            


def bfs(start_node):
    visited_bfs[start_node] = True
    q = deque()
    q.append(start_node)
    
    while q:
        curr_node = q.popleft()
        bfs_answer.append(str(curr_node))
        
        for next_node in graph[curr_node]:
            if next_node not in visited_bfs:
                q.append(next_node)
                visited_bfs[next_node] = True
dfs(V)
bfs(V)

print(' '.join(dfs_answer))
print(' '.join(bfs_answer))
