"""
1,2,3,4,5,1,2,3,4,5,1,2,...
2,1,2,3,2,4,2,5,2,1,2,3....
3,3,1,1,2,2,4,4,5,5,3,3,...
"""
def solution(answer):
    
    pattern_1 = [1,2,3,4,5]
    pattern_2 = [2,1,2,3,2,4,2,5]
    pattern_3 = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0]*3
    
    for i, ans in enumerate(answer):
        if ans == pattern_1[i % len(pattern_1)]:
            scores[0] += 1
        if ans == pattern_2[i % len(pattern_2)]:
            scores[1] += 1
        if ans == pattern_3[i%len(pattern_3)]:
            scores[2] += 1
    
    max_score = max(scores)
    answer = [i+1 for i, s in enumerate(scores) if s == max_score]
    return answer
    
print(solution([1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2])) # [1,2,3]
