answer = 0
N = int(input())
period_list = [0]*(N+1)
reward_list = [0]*(N+1)
dp = [0]*(N+2)

for i in range(1, N+1):
    period, reward = map(int, input().split())
    period_list[i] = period
    reward_list[i] = reward

if period_list[N] + N == N+1: # 마지막날에 상담이 가능한 경우만
    dp[N] = reward_list[N]

for curr_day in range(N-1, 0, -1): # e.g. N = 7 -> 7, 6, 5, ... 1
    consultation_end_day = curr_day + period_list[curr_day]
    
    if consultation_end_day > N+1: # 상담 불가능한 경우
        dp[curr_day] = dp[curr_day+1]
    else: # N+1인 경우도 통과되기떄문에 인덱스 에러 발생
        dp[curr_day] = max(dp[curr_day+1], reward_list[curr_day] + dp[consultation_end_day])

print(dp[1]) # from 첫번째날 to 마지막날 전체 최적 해