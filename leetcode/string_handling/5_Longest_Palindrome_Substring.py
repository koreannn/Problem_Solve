# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         origin_list = list(s)
#         inversed_list = []
#         for i in range(len(origin_list)): 
#             for l in range(len(origin_list)-i):
#                 inversed_list = origin_list[:len(origin_list)-i]
#                 inversed_list = inversed_list[::-1]
#                 if origin_list == inversed_list:
#                     return ''.join(inversed_list)
        

# # test
# print(Solution().longestPalindrome("babad")) # "bab" or "aba"
# print(Solution().longestPalindrome("cbbd")) # "bb"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ''' <시간 초과>
        origin_list = list(s)
        longest_palindrome = ""
        if len(s)<2 or s == s[::-1]:
            return s

        for i in range(len(origin_list)): 
            for l in range(len(origin_list)-i):  # 서브스트링 시작 위치 l
                substring = origin_list[l:l+(i+1)]  # 길이 i+1짜리 서브스트링
                if substring == substring[::-1]:  
                    if len(substring) > len(longest_palindrome):  
                        longest_palindrome = ''.join(substring)
        return longest_palindrome
        '''
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s)<2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result


# Test cases
print(Solution().longestPalindrome("babad"))  # "bab" or "aba"
print(Solution().longestPalindrome("cbbd"))   # "bb"