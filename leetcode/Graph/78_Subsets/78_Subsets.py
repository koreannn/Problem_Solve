import itertools

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subset_list = []
        for i in range(len(nums)):
            subset_i = [list(comb) for comb in itertools.combinations(nums, i)]
            subset_list.append(subset_i)
        
        return subset_list
# test
print(Solution().subsets([1,2,3])) # [[], [1], ... [1,2,3]]
print(Solution().subsets([0])) # [[], [0]]