A = int(input()) # 수열의 크기
A_list = list(map(int, input().split())) # 수열의 숫자들

dp = [1] * A

for i in range(A):
    for j in range(i):
        if A_list[i] > A_list[j]: # 값이 증가하는 경우에만
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))