'''
2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz
'''
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        answer_set = set()
        num_char_mapping = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        # digits 
        
        answer_list = list(answer_set)
        
        return answer_list