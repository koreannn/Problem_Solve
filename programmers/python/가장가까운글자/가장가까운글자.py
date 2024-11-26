def solution(s):
    answer = [-1] * len(s)
    for idx_1 in range(len(s)):
        for idx_2 in range(idx_1+1, len(s)):
            if s[idx_1] == s[idx_2]:
                answer[idx_2] = idx_2-idx_1
    return answer
# test
print(solution("banana"))
print(solution("foobar"))