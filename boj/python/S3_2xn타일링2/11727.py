n = int(input()) # 1 <= n <= 1000
answer = 0

fact_dp = [0]*(n+1)
fact_dp[0] = 1
for i in range(1, n+1):
    fact_dp[i] = fact_dp[i-1]*i

for size3 in range(n//2+1): # size3 = 2x2
    size1 = 0 # 2x1
    size2 = 0 # 1x2
    while (n-2*size3) - 2*size2 >= 0:
        size1 = (n-2*size3) - 2*size2
        answer += fact_dp[size1+size2+size3]//(fact_dp[size1] * fact_dp[size2] * fact_dp[size3])
        size2 += 1

print(answer%10007)