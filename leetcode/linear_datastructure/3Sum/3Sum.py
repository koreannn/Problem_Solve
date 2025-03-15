class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]: # 브루트포스 - 시간복잡도 O(n^3)
        result = set()
        nums.sort()
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (nums[i]+nums[j]+nums[k])==0:
                        # result.append([nums[i], nums[j], nums[k]])
                        result.add((nums[i], nums[j], nums[k]))
                        
        result = list(map(list, result))
        return result
    
# test
print(Solution().threeSum([-1, 0, 1, 2, -1, -4])) # [[-1, -1, 2], [-1, 0, 1]]
print(Solution().threeSum([0, 1, 1])) # []
print(Solution().threeSum([0, 0, 0])) # [0, 0, 0]