```
"""
- 큐: 선입선출
- 주어지는 두 개의 큐는 길이가 같음
    - 주어지는 큐의 길이가 같은거고, 연산 후에도 길이가 같아야한다는 조건은 없음
- 값의 삽입(insert)과 추출(pop)을 최소한의 횟수만큼만 수행하여 두 큐의 합이 같도록 만들기.
    - 삽입과 추출을 묶어서 한 번의 연산으로 간주함
- 본 문제에서 큐는 리스트로 구현함
- 어떻게 해도 같게 만들 수 없는 경우 -> answer = -1

- e.g.
    queue1 = [3,2,7,2] -> 합: 14
    queue2 = [4,6,5,1] -> 합: 16

    방법 1. 
        queue2에서 4,6,5를 순서대로 추출 -> queue1에 삽입 -> 연산 횟수(answer): 3 -> queue1 = [3,2,7,2,4,6,5] / queue2 = [1]
        queue1에서 3,2,7,2를 순서대로 추출 -> queue2에 삽입 -> 연산횟수(answer): 4 -> queue1 = [4,6,5] / queue2 = [1,3,2,7,2]
        총 연산 횟수 7
        
    방법 2.
        queue1에서 3을 추출 -> queue2에 삽입 -> 연산 횟수(answer): 1 -> queue1 = [2,7,2] / queue2 = [4,6,5,1,3]
        queue2에서 4를 추출 -> queue1에 삽입 -> 연산횟수(answer): 1 -> queue1 = [2,7,2,4] / queue2 = [6,5,1,3]
        총 연산횟수 2
"""
```

# 시간 복잡도에서 걸렸던 코드
```python
def solution(queue1, queue2):
    answer = 0
    
    while True:
        if not queue1 or not queue2: # 어떻게 해도 답이 안나오는 경우
            answer = -1
            break
        
        q1_sum = sum(queue1)
        q2_sum = sum(queue2)
        
        if q1_sum == q2_sum:
            break
        elif q1_sum > q2_sum:
            q1_poped = queue1.pop(0)
            queue2.append(q1_poped)
            answer += 1
        else: # q1_sum < q2_sum
            q2_poped = queue2.pop(0)
            queue1.append(q2_poped)
            answer += 1
        
    return answer

# test
print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
print(solution([1, 1], [1, 5])) # -1
```
- 시간 복잡도에서 크리티컬하게 작용한 요소
    - 

# 시간 복잡도를 해결한 코드


```python
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
```

# collections.deque를 쓰지 않을 경우
문제에서 '큐는 배열로 취급한다'라고 되어있는데, 직접적으로 큐를 사용하지 않고 큐처럼 동작하도록 만들라는거같아, collecitons.deque를 쓰지 않고 푸는 방법도 찾아봄.

```python

```