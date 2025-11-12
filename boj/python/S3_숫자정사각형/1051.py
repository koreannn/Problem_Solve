N, M = map(int, input().split()) # 가로 길이, 세로 길이
nums = []
start_length = min(N, M) # 가장 큰 정사각형의 길이
answer = 0

for _ in range(M):
    curr_nums = input()
    nums.append()

for curr_length in range(start_length, 0, -1): # e.g. 3, 2, 1
    for row_start in range(M - start_length + 1): # 행 이동(위아래 이동)
        for col_start in range(N - start_length + 1): # 열 이동(좌우 이동)
            if (nums[row_start][col_start] == nums[row_start][col_start + start_length] == nums[row_start + start_length][col_start] == nums[row_start + start_length][col_start + start_length]) and curr_length > answer:
                answer = curr_length
    
print(answer)