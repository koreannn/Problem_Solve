# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         unique_char = []
#         for char in s:
#             if char in unique_char:
#                 unique_char.clear()
                
#             unique_char.append(char)
#             print(unique_char)
            
#         return len(unique_char)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx = {}
        start = 0
        max_len = 0
        
        for end, char in enumerate(s):
            if char in char_idx and char_idx[char] >= start:
    
# test
print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3 (abc)
print(Solution().lengthOfLongestSubstring("bbbbb")) # 1 
print(Solution().lengthOfLongestSubstring("pwwkew")) # 3 (wke)

# 연속 -> 투포인터 / 연속X -> Dynamic Programming ?