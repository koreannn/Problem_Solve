class Solution:
    def arrayPairSum(self, nums: list[int]) -> int: # 정렬 후 앞에서 두 개씩 Pair를 만드는 방식
        result = 0
        pair = []
        nums.sort()
        
        for num in nums:
            pair.append(num)
            if len(pair) == 2:
                result += min(pair)
                pair = []
                
        return result

# test
