class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        prod = 1
        for num in nums:
            prod *= num
            answer.append(prod)
        return answer
        
print(Solution().productExceptSelf([1, 2, 3, 4])) # [24, 12, 8, 6]
print(Solution().productExceptSelf([-1, 1, 0, -3, 3])) # [0, 0, 9, 0, 0]
