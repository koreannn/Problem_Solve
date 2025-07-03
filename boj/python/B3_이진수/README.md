# 다른 풀이 총 정리

1. `bin()`을 사용한 풀이
```python
t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    curr_bin = bin(n)[2:][::-1]
    curr_answer = []
    
    index = 0
    curr_answer = [str(i) for i in range(len(curr_bin)) if curr_bin[i]=='1']
    answer.append(curr_answer)

for indexes in answer:
    print(' '.join(indexes))
```
- 문자열 뒤집기: `inverted_string = string[::-1]
- 리스트 컴프리헨션의 장점: 가독성이 좋고 속도도 살짝 더 빠르다.



2. 직접 이진수로 변환하기
```python
t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    index = 0
    curr_answer = []
    while n > 0:
        if n%2 == 1: 
            curr_answer.append(str(index))
        n //= 2 
        index+=1
    answer.append(curr_answer)

for indexes in answer:
    print(' '.join(indexes))
```



3. 비트연산자 활용
```python
t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    index = 0
    curr_answer = []
    while n > 0:
        if n&1: # ('n%2==1'과 동일)
            curr_answer.append(str(index))
        n >>= 1 # 오른쪽으로 1칸 shift ('n //= 2'와 동일)
        index+=1
    answer.append(curr_answer)

for indexes in answer:
    print(' '.join(indexes))
```
- `n&1`: 비트 연산자로, AND연산을 수행(n이 홀수일 때 True)