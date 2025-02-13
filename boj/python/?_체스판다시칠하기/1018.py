'''
(0,0) ~ (N-8, M-8)까지 8*8짜리 체스판을 탐색
'''
N, M = map(int, input().split()) # NxM의 판때기
board = []

for _ in range(N):
    board.append(list(input()))


for x in range(N-7):
    for y in range(M-7):
        repaint_W = 0 # 흰색으로 시작하는 체스판을 선택할 경우 색칠해야하는 개수
        repaint_B = 0 # 검은색으로 시작하는 체스판을 선택할 경우 색칠해야하는 개수
        
        for i in range(8): # 8x8을 탐색
            for j in range(8):
                if ()

