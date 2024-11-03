- 처음 봤을 떄 당연히 큐랑 스택 이용하는 문제일줄 알았는데, 굳이 이용할 필요가 없었음
- 그냥 직관적으로 작성하다보니 너무 조잡하게 풀었는데, 정리해서 깔끔하게 풀어보면, 아래와 같은 방식들로 풀 수 있을 듯.

1. 

```python
def solution(food):
    answer = '0'
    for i in range(len(food) - 1, 0, -1): # 3,2,1
        result = str(i) * (food[i] // 2) + result + str(i) * (food[i] // 2)
    return answer

# test case
print(solution([1,3,4,6])) # 각각 0,1,2,3의 개수를 의미 >> food_length = (1+2+3)*2 +1 = 13 > 13//2 = 6 : 가운데(물) 인덱스값
print(solution([1,7,1,2]))
```

- 우연찮게 인덱스값이 채우려는 값이랑 맞아 떨어져서 쓸 수 있는 풀이인듯
- 다만, 단순 문자열 조작을 통해 작성했으므로, 메모리도 효율적이고, 원래 풀이처럼 반복문 중첩이 없어 시간 복잡도도 O(n)(food의 길이)으로 깔끔
- 그냥 여기서 답을 내기 위한 풀이로는 적절할수도 있지만, 단순 문자열 연산으로 답을 내는것이기 때문에, 문자열의 연산량이 많아질수록 비효율적일 수 있음

---

2. 스택과 큐를 활용해서 풀기

처음 떠오른 방법인만큼, 큐랑 스택을 굳이 이용해서도 풀어봤음.

### Stack

```python
def solution(food):
    answer = []
    for i in range(1, len(food)):
        answer.extend([str(i)] * (food[i] // 2))
    answer = ''.join(answer + ['0'] + answer[::-1])
    return answer

# test case
print(solution([1,3,4,6])) # 각각 0,1,2,3의 개수를 의미 >> food_length = (1+2+3)*2 +1 = 13 > 13//2 = 6 : 가운데(물) 인덱스값
print(solution([1,7,1,2]))
```

### Queue

```python
from collections import deque

def solution(food):
    answer = deque()
    for i in range(1, len(food)):
        answer.extend([str(i)] * (food[i] // 2)) # 반쪽만 만들기
    answer = ''.join(answer) + '0' + ''.join(reversed(answer))
    return answer

# test case
print(solution([1,3,4,6])) # 각각 0,1,2,3의 개수를 의미 >> food_length = (1+2+3)*2 +1 = 13 > 13//2 = 6 : 가운데(물) 인덱스값
print(solution([1,7,1,2]))
```

정리하면, 첫번쨰 풀이는 규칙성 찾아서 약간 야매로 푸는 느낌이고, 다시 제대로 풀어보라하면 두 번째 방법 이용할 듯.
