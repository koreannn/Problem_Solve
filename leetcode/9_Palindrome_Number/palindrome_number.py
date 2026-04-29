class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        rev = [x_str[i] for i in range(-1, -len(str(x)) - 1, -1)]
        rev_str = ''.join(rev)
        if x_str == rev_str:
            return True
        else:
            return False