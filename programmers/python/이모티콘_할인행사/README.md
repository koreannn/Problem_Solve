e.g. `10, 20, 30, 40`에서 세 가지 숫자를 뽑아 나열하는 경우의 수

```
10 10 10
10 10 20
10 10 30
10 10 40
10 20 10
10 20 20
...
```

코드로 구현해보자.

1. itertools로 반복 가능한 객체를 만들고, 루프로 돌릴 수 있음
```python
import itertools

numbers = [10, 20, 30, 40]

combs = itertools.product(numbers, repeat=3)
print(combs)

for idx, comb in enumerate(combs):
    print(f"{idx+1}: {comb}")
```

2. dfs로 풀기
깊이 우선 탐색으로 모든 경우의수를 재귀적으로 탐색하는 방식

```python
def dfs(nums, length, curr_answer, result):
    if len(curr_answer) == length:
        result.append(curr_answer[:])
        return
    
    for num in nums:
        curr_answer.append(num)
        dfs(nums, length, curr_answer, result)
        curr_answer.pop()

numbers = [10, 20, 30, 40]
comb_length = 3
answers = []

dfs(numbers, comb_length, [], answers)

for idx, comb in enumerate(answers):
    print(f"{idx+1}: {comb}")
```