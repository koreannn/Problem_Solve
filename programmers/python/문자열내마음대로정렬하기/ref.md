1. 파이썬스럽게 풀기

```python
def solution(strings, n):
    answer = []
    strings.sort(key=lambda x : (x[n], x)) 
    answer = strings
    
    return answer
```

2. 안 파이썬스럽게 풀기

- 한번은 n값에 대한 인덱스를 기준으로 정렬, 한번은 사전순 정렬로 총 두 번 정렬시킴
- 첫 번째 정렬은 직관적으로 정렬해봄
- 두 번째 정렬은 버블정렬 하긴했는데, 다른 정렬로 해도 될듯
