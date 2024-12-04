import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower() # 반환 타입 : str -> str
        # paragraph = paragraph.replace(",", " ")
        
        paragraph_list = [word for word in re.sub(r'[^\w]', ' ', paragraph).split()]
        
        # counts = dict(collections.Counter(paragraph_list)) # 반환 타입 : dict -> collections.Counter
        # 1st. 중복을 제거한 리스트
        non_overlap_list = set(paragraph_list)
        non_overlap_dict = {word: 0 for word in non_overlap_list} 
        print(non_overlap_dict)
        
        # 2nd. 단어별 등장 횟수 value값 기반 카운팅
        for word in non_overlap_dict.keys():
            for i in range(len(paragraph_list)):
                if word == paragraph_list[i]:
                    non_overlap_dict[word] += 1
                    
        non_overlap_dict = dict(sorted(non_overlap_dict.items(), key=lambda x: x[1], reverse=True))
        print(non_overlap_dict)
        
        # 3rd. banned에 포함된 단어 제거
        for banned_word in banned:
            if banned_word in non_overlap_dict:
                non_overlap_dict.pop(banned_word)
        print(non_overlap_dict)
        # if counts.keys()[0] in banned:
        #     counts.pop(counts.keys()[0])
        # return counts.most_common(1)[0][0]
        return list(non_overlap_dict.keys())[0]

# test
print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])) # "ball"
print(Solution().mostCommonWord("a.", [])) # "a"