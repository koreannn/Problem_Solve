def solution(s):
    answer = False
    if (len(s)==4 or len(s)==6):
        answer = True
        for char in s:
            if not char.isdigit():
                answer = False
                break
    return answer
# 정수 0 ~ 9 아스키값 : 48 ~ 57

# test
print(solution("a234"))
print(solution("1234"))