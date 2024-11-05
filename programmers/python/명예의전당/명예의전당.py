def solution(k, score):
    answer = []
    ranking = []
    
    for i in range(len(score)):
        if i < k:
            ranking.append(score[i])
        else:
            if min(ranking) < score[i]:
                ranking.remove(min(ranking))
                ranking.append(score[i])
        answer.append(min(ranking))
    return answer

# test
print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))


