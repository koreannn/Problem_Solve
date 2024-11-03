def solution(k, score):
    answer = []
    
    ranking = sorted(score[:k], reverse=True)
    
    for l in range(k):
        answer.append(ranking[-1])

    for i in range(k, len(score)):
        if ranking[-1] < score[i]:
            ranking.pop()
            ranking.append(score[i])
            ranking = sorted(ranking, reverse=True)
        answer.append(ranking[-1])
    return answer

# test
print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
