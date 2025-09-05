# from collections import deque

# t = int(input())
# answer = []

# for _ in range(t):
#     n, m = map(int, input().split()) # 문서의 개수, 타겟 문서의 위치(인덱스값)
#     importances = list(map(int, input().split()))
    
#     pair = deque((idx, importance) for idx, importance in enumerate(importances))

#     for i in range(len(pair)-1):
#         for j in range(i+1, len(pair)):
#             if pair[j][1] > pair[i][1]:
#                 curr = pair.popleft()
#                 pair.append(curr)
            
#     curr_answer = 1
#     for i in pair:
#         if i[0] == m:
#             break
#         curr_answer += 1
    
#     answer.append(str(curr_answer))

# print('\n'.join(answer))


"""
- 타일의 종류: 1 / 00
- N은 이진수의 크기
    e.g.
    N = 1일 경우 만들 수 있는 타일: 1
    N = 2 -> 00, 11 (2)
    N = 3 -> 001, 100, 111 (3)
    N = 4 -> 0000, 0011, 1001, 1100, 1111 (5)
    N = 5 -> 00001, 00100, 10000, 00111, 10011, 11001, 11100, 11111  (8)
    N = 6 -> (13)
        00을 3개 쓰는 경우 -> 4H0 = 4C0 = 1
        00을 2개 쓰는 경우 -> 3H2 = 4C2 = 6
        00을 1개 쓰는 경우 -> 2H4 = 5C4 = 5
        00을 0개 쓰는 경우 -> 1
- 각 타일의 개수는 신경쓰지 않는다(무한 개 가지고있다고 가정한다)
"""
import sys

input = sys.stdin.readline

N = int(input()) # 이진수의 크기
answer = 0

if N == 1:
    answer = 1
if N == 2:
    answer = 2


pprev, prev = 1, 2
for _ in range(3, N+1):
    answer = (prev + pprev)%15746
    pprev = prev
    prev = answer
count = 3
    
print(answer%15746)