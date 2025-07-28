"""
연산의 종류
    - 앞에서 하나 뽑아내기 
    - 반시계방향으로 회전시키기
    - 시계방향으로 회전시키기
    
1 2 3 4 5 6 7 8 9 10
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
queries = map(int, input().split())

q = deque(range(1, n+1))

def leftcount(queue, target):
    count = 0
    while queue[0] != target:
        queue.rotate(-1)
        count += 1
    
    return count

def rightcount(queue, target):
    count = 0
    while queue[0] != target:
        queue.rotate(1)
        count += 1
        
    return count

answer = 0
for num in queries:
    q_left = deque(q)
    q_right = deque(q)
    
    left = leftcount(q_left, num)
    right = rightcount(q_right, num)
    print(left, right)
    
    # min_count = min(leftcount(q, num), rightcount(q, num))
    # print(leftcount(q, num))
    # print(rightcount(q, num))
    # answer += min_count
    
# print(answer)