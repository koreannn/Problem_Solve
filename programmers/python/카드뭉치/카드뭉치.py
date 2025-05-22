def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1_idx, cards2_idx = 0, 0
    
    for i in range(len(goal)):
        if goal[i] == cards1[cards1_idx]:
            if cards1_idx != len(cards1)-1:
                cards1_idx += 1
        elif goal[i] == cards2[cards2_idx]:
            if cards2_idx != len(cards2)-1:
                cards2_idx += 1
        else:
            answer = 'No'
            break
    
    return answer
