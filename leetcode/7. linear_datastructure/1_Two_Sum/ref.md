풀이는 매우 쉽지만, 최적화된 풀이에 있어서는 깊이 생각해볼만한 가치가 있는 문제입니다.

1. 브루트 포스 방식
```python
class Solution:
    def twosum(self, nums: list[int], target:int) -> list[int]:
        for i in range(nums):
            for j in range(i+1, nums):
                if nums[i]+nums[j] == target:
                    return [i, j]
```
이렇게 풀면, 시간복잡도는 O(n^2)이 됩니다. 매우 비효율적인 풀이이므로, 다른 방법에 대해 고민해야합니다.

2. in연산, index() 사용
```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            if (target-nums[i]) in nums[i+1:]:
                return [nums.index(nums[i]), nums[i+1:].index(target-nums[i])+(i+1)] # 슬라이싱한만큼 다시 더해줘야함
```
이는 브루트포스 방식과 마찬가지로 O(n^2)의 시간복잡도를 갖습니다.

다만, 1번처럼 파이썬 레벨에서 매번 값을 비교하는 방식과 달리, 2번 방식의 in, index연산은 C언어로 구현되어있어, 메모리 접근, 캐시 활용 효율성 등의 측면에서 조금 더 나은 시간복잡도를 가질 수 있습니다.


3. 해시테이블
```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}
        
        for i, num in enumerate(nums):
            nums_dict[num] = i
        
        for i, num in enumerate(nums):
            if (target-num in nums_dict) and (i != nums_dict[target-num]):
                return (i, nums_dict[target-num])
```
딕셔너리는 해시테이블 기반으로 이루어진 자료구조로, 값을 조회하는 시간복잡도에서 O(1)의 복잡도를 가져, 전체 시간복잡도는 O(n)이 됩니다.