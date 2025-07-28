# """
# terms: 약관 종류와 각각에 대한 유효기간
# privacies: 고객들의 약관 동의일과 약관 종류
# 해야하는것: today를 기준으로 봤을 때, 파기해야하는 약관을 "인덱스값+1"로 반환하기

# 2000 <= 년 <= 2022
# """

# def solution(today, terms, privacies):
#     answer = [] # 파기해야하는 약관 (인덱스값+1로 저장)
#     terms_to_dict = {}
    
#     today_to_day = today.split(".")
    
    
    
#     return answer


# # test
# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])) # [1, 3]

test = "2022.05.19"
print(test.split('.'))