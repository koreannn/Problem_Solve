"""
중요도 숫자가 높을수록 중요도가 높음
타겟 문서 뒤로, 해당 문서의 중요도보다 높은 종요도의 문서가 없으면 됨
정렬 기준: 중요도가 높은 순서대로 & 중요도가 동일할 경우, 인덱스값이 작은 순서대로

"""
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
answer = []

for _ in range(t):
    n, m = map(int, input().split()) # n: 문서의 개수 / m: 찾고자 하는 문서가 몇번째에 놓여있는지를 나타내는 정수
    sequences = list(map(int, input().split())) # 각 문서의 중요도 (중요도값이 클수록 더 먼저 출력됨)
    queue = deque([(idx, priority) for idx, priority in enumerate(sequences)])
    
    count = 0
    while queue:
        curr = queue.popleft()
        if any(curr[1] < q[1] for q in queue): # 맨 앞의 문서보다 중요도가 높은 문서가 있을 경우
            queue.append(curr) # 뒤로 가기
        else:
            count += 1
            if curr[0] == m: # 찾고자 하는 문서라면
                break
    
    answer.append(str(count))


print('\n'.join(answer))

