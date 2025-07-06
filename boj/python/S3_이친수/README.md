시간 복잡도를 고려하면서 풀기

1. 틀린 풀이(시간 초과)
```python
n = int(input()) # 자리수 (e.g. n=2 -> ~3 / n=3 -> ~7)
num = 2**n-1
length = len(bin(num)[2:])
answer = 0

for curr_num in range(1, num+1):
    is_answer = True
    curr_bin = bin(curr_num)[2:]
    
    if len(curr_bin) < length:
        continue # 자릿수가 짧은 경우 '0xxxx'꼴이므로 pass
    
    prev = curr_bin[0]
    for i in range(1, len(curr_bin)):
        if (curr_bin[i] == prev) and prev == '1':
            is_answer = False
            break
        prev = curr_bin[i]
        
    if is_answer:
        answer+=1
        
print(answer)
```
- 완전 탐색으로 풀면 시간복잡도가 $O(2^n)$ → 시간 초과
- 백트래킹으로 탐색 횟수를 좀 줄인다고 해도 지수승이므로 시간복잡도가 여전히 큼


2. 올바른 풀이
```python
n = int(input())
answer = 0
if n <= 2:
    answer = 1
else:
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[n]
    
    print(answer)
```
- 지수승의 시간복잡도를 해결해야함 → 지수승의 시간복잡도를 갖는 부분은 첫 번쨰 for문이므로, 첫 번쨰 for문을 일단 없애야함
- n값에 따른 수열을 나열하다보면, 피보나치 관계식을 갖는다는걸 알 수 있음($f_n = f_{n-1} + f_{n-2}$)
