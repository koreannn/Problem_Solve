n = int(input())
t_list = []
p_list = []
dp = [0]*(n+1) # dp[i]: i번째 날에 퇴사직전까지 가능한 최대 수익

for _ in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)
    
for i in range(n-1, -1, -1): # n-1, n-2, ... 0
    if (n-i) < t_list[i]: # 상담 기긴이 남은 퇴사일보다 큰 경우(상담 불가)
        dp[i] = dp[i+1]
    else: 
        dp[i] = max(dp[i+1], p_list[i]+ dp[i + t_list[i]])

print(dp[0])