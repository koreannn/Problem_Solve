def solution(name, yearning, photo):
    answer = []
    name_score_pair = {}
    for i in range(len(name)):
        name_score_pair[name[i]] = yearning[i]
        
    for name_list in photo:
        curr = 0
        for name in name_list:
            if name in name_score_pair:
                curr += name_score_pair[name]
        answer.append(curr)
    return answer

# test
print(solution(
    ["may", "kein", "kain", "radi"], 
    [5, 10, 1, 3],
    [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
)) # [19, 15, 6]