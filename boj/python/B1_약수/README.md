두 가지 방법을 생각했는데,

1. `math.lcm`으로 최소공배수를 찾는 것

```python
import sys
from math import lcm
input = sys.stdin.readline

num_of_real_div = int(input()) # 진짜 약수의 개수
real_div = map(int, input().split()) # '진짜 약수'들
sorted_real_div = sorted(real_div)

answer = lcm(*sorted_real_div)

print(answer)
```

2. 진짜 약수들의 $최솟값*최댓값$

```python
import sys
from math import lcm
input = sys.stdin.readline

num_of_real_div = int(input()) # 진짜 약수의 개수
real_div = map(int, input().split()) # '진짜 약수'들
sorted_real_div = sorted(real_div)

answer = sorted_real_div[0] * sorted_real_div[-1]

print(answer)
```

둘 다 100% 똑같은 방식이라고 생각했는데, 1번은 틀렸다고 뜨고 2번은 맞다고 뜸