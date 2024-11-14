def solution(n):
    answer = 0
    while(n>0):
        answer = answer + n%10
        n = n//10
    return answer

# test
print(solution(123)) 
print(solution(987))