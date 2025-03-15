'''
e.g. 13 = 11+1+1 -> 11은 13의 생성자
'''
N = int(input())

# 배열 만들고 하나씩 올라가면서 각 생성자 값 저장하기: X (메모리 초과되는듯)
# 원하는 값에 대한 생성자 매칭될때까지 반복문 돌리기: O
result = 0
for i in range(1, N+1):
    sum_digits = sum(map(int, str(i)))  # 각 자릿수의 합
    decomp_sum = i + sum_digits  # 분해합(현재 수 + 각 자릿수의 합)
    
    if decomp_sum == N:
        result = i
        break

print(result)

