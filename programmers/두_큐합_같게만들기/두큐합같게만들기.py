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