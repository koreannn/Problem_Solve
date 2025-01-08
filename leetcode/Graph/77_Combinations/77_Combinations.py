import itertools
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        data = [i for i in range(1,n+1)]
        print(data)
        combinations = [list(comb) for comb in itertools.combinations(data, k)]
        return combinations
# test
print(Solution().combine(4,2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(Solution().combine(1,1)) # [[1]]