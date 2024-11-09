# 틀린풀이(메모리 초과)

```python
n = int(input())
num = []

for i in range(n):
    num.append(int(input()))
    
num.sort()
print(num)
```

찾아보니 두 가지 문제가 있다고 하는데


1. `input()`으로 값을 입력받지 말고, `sys.stdin.readline()`으로 받아야한다고 하던데 이건 C였으면 별 문제는 안됐을듯. 그냥 파이썬이라서 문제인것
`sys.stdin.readline()`이 `input()`보다 메모리 관점에서 더 효율적인 이유는
- 미리 할당된 버퍼를 사용하므로 추가적인 메모리 할당이 적다
- 메모리 할당, 해제의 오버헤드가 적다
이런 장점이 있다는데, 작은 입력에서는 큰 차이가 없다고 함.

이거 하나만 수정해서 다시 제출했는데, 아직 메모리 초과 뜸
```python
import sys

n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))
    
num.sort()
print(num)
```
(이게 문제는 아니었나봄)

2. `num = []`

결과적으로 이게 핵심이었는데,
문제 조건을 보면 1<n<10000000000 인가로 범위가 지정되어있고, 값의 범위는 10000까지 제한되어있는데, `num = []`으로 n개만큼 모든 숫자를 받아버리게 하면, 엄청나게 많은 숫자를 
리스트에 집어넣는 테스트 케이스가 있나보다. 그래서 `계수 정렬(Counting Sort)`방식을 이용해야한다고 함.

값을 받는 메모리 공간을 10001개로 미리 한정해두고, 각 정수값마다의 출현 빈도를 Count한다. 그리고 간단히 0번 인덱스부터 10000번까지 내려가면서(이러면 정렬 할 필요도 없음), 해당 값이 몇 번 등장했는지에 맞게 그대로 반복 출력만 해주면 됨.

```python
import sys

n = int(sys.stdin.readline())
count = [0]*10001

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1
    
for idx in range(len(count)):
    if count[idx] != 0:
        for _ in range(count[idx]):
            print(idx)
```


