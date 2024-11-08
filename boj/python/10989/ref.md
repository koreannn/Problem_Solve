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


1. input()으로 값을 입력받지 말고, sys.stdin.readline()으로 받아야한다고 하던데 이건 C였으면 별 문제는 안됐을듯. 그냥 파이썬이라서 문제인것
sys.stdin.readline()이 input()보다 메모리 관점에서 더 효율적인 이유는
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

2. 

