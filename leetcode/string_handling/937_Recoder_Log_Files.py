import re
class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        '''
        > 일단, let_log가 dig_log보다 앞에 와야 함
        
        > let_log : 문자로만(소문자로만)이루어진 로그
            1. 내용 기준으로 사전순 정렬 시켜야 함
            2. 내용이 같다면, 식별자(let뒤에 붙어있는 숫자) 기준으로 사전순 정렬 시켜야 함
        
        dig_log : 숫자로만 이루어진 로그
            원래 순서를 유지시키면 됨
        '''
        # let_log 분리
        let_log = []
        dig_log = []
        for log in logs:
            if ord(log[-1]) >= 48 and ord(log[-1]) <= 57:
                dig_log.append(log)
            else:
                let_log.append(log)
        '''
        for log in logs:
            if log.split()[1].isdigit():
                dig_log.append(log)
            else:
                letter_log.append(log)
        '''
        # sorted_let_log = sorted(let_log, key=lambda x: (x.split()[1:], re.findall(r'\d+', x.split()[0])))
        sorted_let_log = sorted(let_log, key=lambda x: (x.split()[1:], x.split()[0]))
        return sorted_let_log + dig_log

# test
print(Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])) # ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
print(Solution().reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])) # ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
