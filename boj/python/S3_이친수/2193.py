n = int(input())
answer = 0
if n <= 2:
    answer = 1
else:
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[n]
    
print(answer)