# a : 교환비율
# b : 받는 콜라의 개수
# n : 보유중인 빈 병
def solution(a, b, n):
    tmp = 0 # 해당 루프마다 받는 콜라의 개수
    answer = 0
    while(n>=a):
        tmp = n//a
        n %= a
        n += tmp*b
        answer += tmp*b
    return answer

# test code
print(solution(2,1,20)) # a, b, n
print(solution(3,1,20))