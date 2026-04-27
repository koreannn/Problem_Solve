def solution(cap, k, score, m): # 받을 수 있는 최대 점수, 나의 현재 점수, 전처 점수 리스트(내림차순 정렬되어있음), 커트라인 등수
    answer = -1 # 점수가 바뀐 사람의 수(최소한으로)
    higher_scores = [s for s in score if s > k]
    num_higher = len(higher_scores)
    
    if num_higher < m: # 이미 본선 진출권인 경우
        return 0
    
    remove_count = num_higher - (m - 1)
    


# test
print(solution(100, 70, [95, 90, 80, 80, 80, 70, 70, 30, 10], 4)) # 출력: 3
print(solution(100, 82, [100, 97, 97, 92, 87, 77, 77, 72, 72], 4)) # 출력: 4