from collections import Counter

class Solution:
    def getbeauty(self, s: str) -> int:
        str_cnt = Counter(s)
        max_cnt = 0
        min_cnt = len(s)
        
        for key in str_cnt.keys():
            if str_cnt[key] < min_cnt:
                min_cnt = str_cnt[key]
            if str_cnt[key] > max_cnt:
                max_cnt = str_cnt[key]
        if min_cnt == len(s):
            return 0
        
        return max_cnt - min_cnt
    
    def beautySum(self, s: str) -> int:
        answer = 0
        for window_size in range(3, len(s) + 1):
            for i in range(len(s) - window_size + 1):
                curr_answer = self.getbeauty(s[i:i + window_size])
                answer += curr_answer
            
        return answer

print(Solution().beautySum("aabcb"))
print(Solution().beautySum("aabcbaa"))