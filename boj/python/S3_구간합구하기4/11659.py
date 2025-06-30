n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = []
pre_sum = [0]*(n+1)

for i in range(1, n+1):
    pre_sum[i] = pre_sum[i-1] + nums[i-1]
    
for _ in range(m):
    start, end = map(int, input().split())
    curr_sum = pre_sum[end] - pre_sum[start-1]
    answer.append(str(curr_sum))

print('\n'.join(answer))