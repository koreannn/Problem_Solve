class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # 1. 재귀로 풀기
        # 2. 반복문 내에서 (중복을 허용해서) 완전탐색하기


# test
print(Solution().combinationSum([2,3,6,7], 7)) # [[2,2,3], [7]]
print(Solution().combinationSum([2,3,5], 8)) # [[2,2,2,2], [2,3,3], [3,5]]
print(Solution().combinationSum([2], 1)) # []