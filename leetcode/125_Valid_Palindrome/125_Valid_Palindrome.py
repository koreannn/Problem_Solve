class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        char_list = []
        for char in s:
            if ord(char) < 65 or ord(char) > 122:
            # if not char.isalnum():
                continue
            char_list.append(char)
        print(char_list)
        inversed_char_list = char_list[::-1]
        # inversed_char_list = list(reversed(char_list))
        print(inversed_char_list)
        return char_list == inversed_char_list

# test
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))