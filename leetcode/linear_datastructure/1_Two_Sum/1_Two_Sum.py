class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]

# test
print(Solution().twoSum([2,7,11,15], 9))  # [0,1]
print(Solution().twoSum([3,2,4], 6)) # [1,2]
print(Solution().twoSum([3,3], 6)) # [0,1]

'''
< 1. 브루트 포스 방식 : 가능한 모든 경우를 무작위로 시도해서 정답을 찾는 방식 >
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
- 시간 복잡도 : O(n^2)

< 2. target에서 n값을 뺴는 방식 >
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i+1:]:
                return nums.index(n), nums[i+1:].index(complement) + (i+1)
- 시간 복잡도 : O(n) (in 연산)

< 3. 첫 번째 수를 뺸 결과 키 조회 >
        nums_map = {}
        for i, n in enumerate(nums):
            nums_map[n] = i
        
        for i, n in enumerate(nums):
            if target - n in nums_map and i != nums_map[target - n]:
                return [i, nums_map[target - n]]
- 시간 복잡도 : O(n) (in 연산)

< 4. 조회 구조 개선 >
        nums_map = {}
        for i, n in enumerate(nums):
            if target - n in nums_map:
                return [nums_map[target - n], i]
            nums_map[n] = i
'''