class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}  # 닫는 괄호를 여는 괄호에 매핑

        for char in s:
            if char in mapping:  # 닫는 괄호일 경우
                top_element = stack.pop() if stack else '#'  # 스택이 비어있으면 '#' 반환
                if mapping[char] != top_element:  # 짝이 맞는지 확인
                    return False
            else:  # 여는 괄호는 스택에 추가
                stack.append(char)
        
        return not stack  # 스택이 비어있으면 True, 아니면 False
    
# test
print(Solution().isValid("()")) # True
print(Solution().isValid("()[]{}")) # True
print(Solution().isValid("(]")) # False
print(Solution().isValid("([])")) # True
print(Solution().isValid("([)]")) # False