'''
(0,0) ~ (N-8, M-8)까지 8*8짜리 체스판을 탐색
'''
N, M = map(int, input().split())  # NxM의 판때기 (N이 행의 개수)
board = []

for _ in range(N):
    board.append(input())

min_val = 32

for x in range(N-7):
    for y in range(M-7):
        # 8x8 영역의 각 행을 슬라이싱
        test_board = [row[y:y+8] for row in board[x:x+8]]
        white = sum(row.count('W') for row in test_board)
        
        if 32-white < min_val:
            min_val = 32-white
        
print(min_val)


