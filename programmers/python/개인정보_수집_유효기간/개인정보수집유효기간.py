"""
terms: 약관 종류와 각각에 대한 유효기간
privacies: 고객들의 약관 동의일과 약관 종류
해야하는것: today를 기준으로 봤을 때, 파기해야하는 약관을 "인덱스값+1"로 반환하기

2000 <= 년 <= 2022
"""

def day_translator(date: str) -> int: # "20xx.xx.xx" -> xxxx(일) 로 변환하는 함수
    day_list = list(map(int, date.split('.')))
    day = (day_list[0] - 2000)*12*28 + day_list[1]*28 + day_list[2]
    return day



def solution(today, terms, privacies):
    answer = [] # 파기해야하는 약관 (인덱스값+1로 저장)
    terms_to_dict = {} # {A: xxx, B: yyy ... } (일 단위로 변환하여 저장)
    
    today_to_day = day_translator(today)
    
    for term in terms:
        kind, available_date = term.split()
        
        if kind in terms_to_dict:
            continue
        
        terms_to_dict[kind] = int(available_date)*28
    
    
    check_index = 1
    for privacy in privacies:
        date, kind = privacy.split()
        date = day_translator(date)
        
        if today_to_day - date >= terms_to_dict[kind]: # 유효기간이 지났을 경우
            answer.append(check_index)
            
        check_index += 1
    
    return answer


# test
print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])) # [1, 3]
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])) # [1, 4, 5]
