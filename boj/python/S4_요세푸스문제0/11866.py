from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n+1))
result = []

while queue:
    queue.rotate(-(k-1))
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")

"""
rotate(1): 시계방향으로 1칸 회전
rotate(-1): 반시계 방향으로 1칸 회전
"""