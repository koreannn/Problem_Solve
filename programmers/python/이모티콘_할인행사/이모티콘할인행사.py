"""
e.g.

사용자 1, 2에 대해
    - 1은 40%이상 할인하는 이모티콘을 모두 구매 / 토탈 구매 비용이 10000원 이상이라면 구매가 아닌 구독을 진행
    - 2는 25%이상 할인하는 이모티콘을 모두 구매 / 토탈 구매 비용이 10000원 이상이라면 구매가 아닌 구독을 진행
이 떄, 아래 예시를 보면
    1. 
    - 이모티콘 1: 7000 / 이모티콘 2: 9000 에 대해, 둘 다 할인율 40%
    - 사용자 1은 모두 구매 / 사용자 2도 모두 구매 -> 각각 9600, 9600원 지불 -> 10000원 이하이므로 구독은 안함
    
    2. 
    - 이모티콘 1: 7000 / 이모티콘 2: 9000에 대해, 각각 할인율 30%, 40%
    - 사용자 1은 이모티콘 2만 구매 / 사용자 2는 둘 다 구매 -> 각각 5400, 10300원 지불 -> 사용자 2는 구독
    
    
변수설명
users: [[40, 10000], [25, 10000], ...] 각 사용자의 할인율과 구독기준비용 / users[i]는 사용자 i+1의 정보를 의미
emoticons: [7000, 9000, ..] 각 이모티콘의 비용
n: 유저 명수 (1 <= <= 100)
m: 이모티콘 개수 (1 <= <= 7)

반환해야하는것: (행사 목적을 최대한으로 달성했을 떄의)구독자 수와 이모티콘 매출액
    행사 목적을 최대한으로 달성하는 것: 
        1. 구독자를 최대한 늘리는것 (우선순위)
        2. 이모티콘 판매액을 최대한 늘리는것
        각 이모티콘의 할인율은 10, 20, 30, 40% -> 이모티콘마다 다름
        
풀이 방식:
    각 이모티콘에 가장 높은 할인율을 적용해보고, 가장 싼 이모티콘 할인율부터 낮춰본다.
    e.g.
    [[40, 10000], [25, 10000]] & [7000, 9000]
    1. 40%, 40% -> 9600, 9600 -> 구독0명, 금액 9600*2원
    2. 30%, 40% -> 5400, 구독 -> 구독1명, 금액 5400원
    3. 20%, 40% -> 5400, 5400 -> 구독0명, 금액5400*2원


"""

def solution(users, emoticons):
    answers = []
    sorted_emo = sorted(emoticons) # 오름차순 정렬된 이모티콘 가격
    sorted_emo_dict = {price: 40 for price in sorted_emo}
    idx = 0 # 할인율 낮출 이모티콘 탐색용 인덱스
    
    for _ in range(len(emoticons)*4): # 각각에 대해  40%, 30%, 20%, 10%를 모두 적용해보아야하므로, *4
        curr_sales_amount = 0
        curr_subscribers = 0
        
        for person in users:
            threshold = 0 # 그 사람이 구독을 할지말지 결정되는 금액
            for price in sorted_emo_dict:
                if person[0] <= sorted_emo_dict[price]: # 그 사람의 기준보다 더 많이 할인할 경우에만
                    threshold += price * ((100 - sorted_emo_dict[price]) / 100.0)
            
            if threshold >= person[1]:
                curr_subscribers += 1
            else:
                curr_sales_amount += threshold
                
        answers.append([curr_subscribers, curr_sales_amount])
        
        # 할인율 낮추기(싼 이모티콘부터)
        if sorted_emo_dict[sorted_emo[idx]] == 10:
            idx += 1
        else:
            sorted_emo_dict[sorted_emo[idx]] -= 10
        
    # answers 정렬
    answers.sort(key=lambda x: (x[0], x[1]), reverse=True)
        
    return answers[0]


# Test
print(solution([[40, 10000], [25, 10000]], [7000, 9000])) # [1, 5400]
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])) # [4, 13860]
