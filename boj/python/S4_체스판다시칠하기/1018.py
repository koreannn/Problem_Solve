n, m = map(int, input().split()) # 8이상 50이하
board = [input() for _ in range(n)] # 한 행씩 칠하기

min_repaint = float('inf')

for i in range(n-7): # 세로 시작 지점 (몇 번째 열?)
    for j in range(m-7): # 가로 시작 지점 (몇 번째 행?)
        count_b = 0 
        count_w = 0 # 흰색을 검은색으로 바꾸는 경우, 검은색을 흰색으로 바꾸는 경우 둘 다 센 다음, 더 작은 값을 갖는 경우로 선택
        
        for x in range(8):
            for y in range(8):
                curr = board[i+x][j+y] # 색칠을 할 지점
                
                if (x+y)%2 == 0: # 시작점을 기준으로 0, 2, 4, 6 열 또는 행
                    if curr!='B': 
                        count_b += 1
                    if curr!='W':
                        count_w += 1
                else: # 시작점을 기준으로 1, 3, 5, 7 열 또는 행
                    if curr!='W':
                        count_b += 1
                    if curr!='B':
                        count_w += 1
        
        min_repaint = min(min_repaint, count_b, count_w)

print(min_repaint)