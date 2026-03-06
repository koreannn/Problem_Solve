from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        answer = 0
        s_counter = Counter(s) 
        t_counter = Counter(t) # s에 맞춰서 t를 바꿔줘야함
        
        for char in s_counter:
            if t_counter[char] < s_counter[char]:
                answer += s_counter[char] - t_counter[char]
        return answer

# test
print(Solution().minSteps("bab", "aba")) # 1
print(Solution().minSteps("leetcode", "practice")) # 5
print(Solution().minSteps("anagram", "mangaar")) # 0