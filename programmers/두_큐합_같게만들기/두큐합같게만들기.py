from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    
    if (sum1+sum2)%2 != 0:
        answer = -1
        return answer
    
    limit = (len(q1)+len(q2))*2
    
    while answer <= limit:
        if sum1 == sum2:
            return answer
        elif sum1 > sum2:
            q1_poped = q1.popleft()
            sum1 -= q1_poped
            
            q2.append(q1_poped)
            sum2 += q1_poped
        else: # sum1 < sum2
            q2_poped = q2.popleft()
            sum2 -= q2_poped
            
            q1.append(q2_poped)
            sum1 += q2_poped
            
        answer += 1
        
    return -1

# test
print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
print(solution([1, 1], [1, 5])) # -1


"""
교훈
- 특별한 알고리즘은 없음. 그냥 구현 문제
- variance는 어디서 추출하고 넣을지가 action의 전부임. 이것만 잘 생각하면 된다.
    - 이에 따라 합이 더 큰 큐에서 더 작은 큐에 값을 뽑아서 넣어주면 됨
    - 다만 넣고 뺴는 작업을 "언제까지" 하느냐가 문제 -> 기준을 잡아야 한다.
        - 각각 하나씩 빼고 하나씩 넣어서, 서로 완전히 바뀌는데까지 걸리는 횟수를 리미트로 잡으면 됨 -> len(queue1)+len(queue2)
"""