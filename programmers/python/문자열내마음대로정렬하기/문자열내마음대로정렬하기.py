# n값(문자열 내의 인덱스값)을 기준으로 사전순 정렬한다
# n값에 대한 문자가 동일하다면, 사전순 정렬한다
def solution(strings, n):
    answer = []
    min_string = strings[0]
    
    # 1. n값 기준 정렬
    for _ in range(len(strings)):
        min_char = 'z'
        for string in strings:
            if min_char > string[n]:
                min_string = string
                min_char = string[n]
            
        answer.append(min_string)
        strings.remove(min_string)
    # 2. 사전순 정렬 (버블 정렬로 해봤음)
    for i in range(len(answer)-1):
        for l in range(len(answer)-1-i):
            if answer[l][n] == answer[l+1][n]:
                if answer[l] > answer[l+1]: # 오름차순(사전순) 정렬
                    answer[l], answer[l+1] = answer[l+1], answer[l]
    
    return answer

# test
print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))


