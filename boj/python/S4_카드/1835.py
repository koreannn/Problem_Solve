"""
e.g. n=4 (n<=1000)
첫 번째: 1번 나와야 함
두 번째: 2번 나와야 함
세 번째: 3번 나와야 함
네 번째: 4번 나와야 함

맨 앞의 카드를 맨 뒤로 보낸다.
그 후 맨 앞의 카드를 꺼냈을 떄 1이 나와야 한다.

거꾸로 따라가기
4를 앞으로 붙임 -> 4를 뒤로 보냄  : 4
-> 3을 앞으로 붙임 -> 3을 뒤로 보냄 : [3,4] -> [4,3]
-> 2를 앞으로 붙임 -> 2를 뒤로 보냄 : [2,4,3] -> [4,3,2]
-> 1을 앞으로 붙임 -> 1을 뒤로 보냄 : [1,4,3,2] -> [4,3,2,1]
"""
from collections import deque
n = int(input())
answer = deque()

for num in range(n, 0, -1):
    answer.appendleft(num)
    tmp = answer[-1]
    answer[-1] = answer[0]
    answer[0] = tmp

for num in answer:
    print(num, end=' ')