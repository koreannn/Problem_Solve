N = int(input()) # 계단의 개수
stairs_scores = [0] + [int(input()) for i in range(N)] # 각 계단의 점수

dp = [0]*(N+1) # dp[0] ~ dp[N] : "각 계단에 도달했을 때 최대 점수"

dp[1] = stairs_scores[1]
if N>=2: 
    dp[2] = stairs_scores[1] + stairs_scores[2] # dp[2] : "2번째 계단에 도달했을 때 최대 점수" 이므로, stairs_score[1]+stairs_score[2]와 같이 정해야 함.
for i in range(3, N+1):
    dp[i] = max(dp[i-2], dp[i-3]+stairs_scores[i-1]) + stairs_scores[i]
# dp[i-2] : 두칸 전의 계단을 밟고, 마지막 계단을 밟을 경우
# dp[i-3]+stairs_scores[i-1] : 세 칸 전의 계단을 밟고, 마지막 계단 전의 계단을 밝고, 마지막 계단을 밟을 경우

print(dp[N])