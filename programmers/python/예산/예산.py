def solution(d, budget):
    # d : 부서별 신청 금액
    # budget : 회사가 가지고있는 총 지원 금액
    answer = 0
    sorted_list = sorted(d)
    for money in sorted_list:
        if money > budget :
            break
        budget = budget - money
        answer += 1
    return answer

# test
print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))