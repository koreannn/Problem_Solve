N, M = map(int, input().split())
left, right = 0, 0
answer = 0
curr_sum = 0

nums = list(map(int, input().split()))

for right in range(N):
    curr_sum += nums[right]
    
    while curr_sum >= M:
        if curr_sum == M:
            answer += 1
        curr_sum -= nums[left]
        left += 1

print(answer)


# while right <= N:
#     curr_sum = sum(nums[left : right]) # 슬라이싱 및 sum연산 -> 비효율적
    
#     if curr_sum == M:
#         answer += 1
#         right += 1
#     elif curr_sum < M:
#         right += 1
#     else: # curr_sum > M
#         left += 1
        
# print(answer)
