class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        '''
        s = list(reversed(s))
        또는
        s = s[::-1]
        in-place 연산이 아님 (새로운 리스트 객체를 생성하고, s가 이걸 새로 참조하도록 만듬)
        
        기존 리스트의 내용을 직접 역순으로 수정하려면
        s[:] = s[::-1] 
        '''
        s[:] = s[::-1]
        return s
        
'''
<다른 풀이(가연 풀이)>
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
'''

# test
print(Solution().reverseString(["h","e","l","l","o"])) # ["o","l","l","e","h"]
print(Solution().reverseString(["H","a","n","n","a","h"])) # ["h","a","n","n","a","H"]
