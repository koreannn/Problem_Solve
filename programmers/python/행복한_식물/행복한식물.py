"""
2024 네이버 신입 공채 문제

- emotions: 각 식물들의 초기 상태 -> e.g. emotions[i]: i+1번째 식물의 초기 상태
- 값이 0보다 클 경우 기분이 좋은것
- orders: 각 사이클마다 물을 주는 식물 번호 -> e.g. orders[i]: i+1번쨰 사이클에 해당 식물에게 물을 주었음을 의미
    e.g. emotions = [2,3,1,2] / orders = [3,1,2,1,4,1]

- 한 사이클이 지날떄마다 상태값이 1씩 감소(0이 되면 더이상 기분이 좋지 않음)
- 한번 0이 되면 물을 줘도 기분이 좋아지지 않음

"""

def solution(emotions, orders) -> list:
    answer = 0
    
    for i in range(len(orders)):
        curr = 0
        for emo in emotions:
            emo -= 1
        emotions[orders[i]] += 1
        
        for emo in emotions:
            if emo > 0:
                curr += 1
        answer.append(curr)
    
    return answer

# test
print(solution([2,3,1,2], [3,1,2,1,4,1])) # [4, 2, 2, 2, 2, 1]

