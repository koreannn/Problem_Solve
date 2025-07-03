# 시간 복잡도 신경쓰기

풀이 1.
```python
n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = []

for _ in range(m):
    start, end = map(int, input().split())
    curr = 0
    for i in range(start-1, end):
        curr += nums[i]
    answer.append(str(curr))
    
print("\n".join(answer))
```
- 주요 연산
    - 첫 번째 for문 → O(m)
    - 두 번째 for문 → O(n) (최악의 경우)
    - 전체 시간복잡도 → O(m*n)



풀이 2. 
```python
n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = []

nums_acc = [0]*(n+1)
for i in range(1, n+1):
    nums_acc[i] = nums_acc[i-1]+nums[i-1]

for _ in range(m):
    start, end = map(int, input().split())
    curr = nums_acc[end] - nums_acc[start-1]
    answer.append(str(curr))
    
print("\n".join(answer))
```
- 주요 연산
    - 첫 번째 for문 → O(n)
    - 두 번째 for문 → O(m)
    - 전체 시간복잡도 → O(n+m)
