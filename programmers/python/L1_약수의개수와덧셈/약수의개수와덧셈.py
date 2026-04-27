"""
약수의 개수가 홀수개인 수는 완전제곱수밖에 없음
"""
import math

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if math.sqrt(num) == int(math.sqrt(num)):
            answer -= num
        else:
            answer += num
    return answer

# test
print(solution(13, 17)) # 43
print(solution(24, 27)) # 52