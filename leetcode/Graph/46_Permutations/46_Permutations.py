import itertools

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = [list(permutation) for permutation in itertools.permutations(nums)]
        return permutations

# test
print(Solution().permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution().permute([0,1])) # [[0,1],[1,0]]
print(Solution().permute([1])) # [[1]]