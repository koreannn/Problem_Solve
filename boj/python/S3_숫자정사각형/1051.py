N, M = map(int, input().split()) # 세로 길이, 가로 길이
nums = [input().strip() for _ in range(N)]
start_length = min(N, M) # 가장 큰 정사각형의 길이
answer = 0

for curr_length in range(start_length, 0, -1): # e.g. 3, 2, 1
    for col_start in range(M - curr_length + 1): # 열 이동(좌우 이동)
        for row_start in range(N - curr_length + 1): # 행 이동(위아래 이동)
            # 정사각형의 네 꼭지점
            lt = nums[row_start][col_start] 
            lb = nums[row_start + curr_length - 1][col_start]
            rt = nums[row_start][col_start + curr_length - 1]
            rb = nums[row_start + curr_length - 1][col_start + curr_length - 1]
            
            if lt == lb == rt == rb:
                print(curr_length ** 2)
                exit(0)