# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         sorted_strs = []
#         Anagrams_word_position = []
#         count = 0
#         for i in range(len(strs)):
#             sorted_strs.append(''.join(sorted(strs[i])))
        
#         # 애너그램끼리 인덱스 위치 저장하기    
#         for i in range(len(sorted_strs)):
#             Anagrams_word_position.append(i)
#             for j in range(i+1, len(sorted_strs)-i-1):
#                 if sorted_strs[i] == sorted_strs[j]:
#                     Anagrams_word_position.append(j)
#             Anagrams_word_position.append("end")
#         # print(Anagrams_word_position)
#         # for l in range(len(sorted_strs)):
#         #     for j in range(len(sorted_strs)-i-1):
#         #         if sorted_strs[l] == sorted_strs[j]:
#         #             Anagrams_word_position.append(j)
                    
            
#         print(sorted_strs)
            
# # test
# print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) # [["ate","eat","tea"],["nat","tan"],["bat"]]
# print(Solution().groupAnagrams([""])) # [[""]]
# print(Solution().groupAnagrams(["a"])) # [["a"]]

a = [1,2,3,4,5]
print()