N, M = map(int, input().split()) # 1<= <= 10,000 / 1<= <= 300,000,000
N_list = list(map(int, input().split()))
answer = 0

# 올바른 풀이
left, right = 0, 0
curr = 0

while True:
    if curr >= M:
        if curr == M:
            answer += 1
        curr -= N_list[left]
        left += 1
    
    else:
        if right == N:
            break
        curr += N_list[right]
        right += 1

print(answer)

# dfs를 이용한 풀이 (시간복잡도떄문에 안됨)
# def dfs(curr_idx, curr_sum):
#     if curr_sum == M:
#         global answer
#         answer += 1 
#         return
#     if curr_idx == N or curr_sum > M:
#         return
    
#     dfs(curr_idx + 1, curr_sum + N_list[curr_idx])
    
# for start in range(N):
#     dfs(start, 0)

# print(answer)

# 위 dfs가 단순 반복문이랑 뭐가 다름?
# for start in range(N):
#     curr_sum = N_list[start]
#     for j in range(start + 1, N):
#         if curr_sum == M:
#             answer += 1
#             break
#         if curr_sum > M:
#             continue
#         curr_sum += N_list[j]

# print(answer)



