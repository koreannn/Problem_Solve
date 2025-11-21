board = [list(map(int, input().split())) for _ in range(9)]

def check(board, curr_row, curr_col, num) -> bool:
    # 행 검사
    for i in range(9):
        if board[curr_row][i] == num:
            return False
    
    # 열 검사
    for i in range(9):
        if board[i][curr_col] == num:
            return False
    
    # 3x3 box 검사
    box_row = (curr_row // 3) * 3
    box_col = (curr_col // 3) * 3
    for row in range(3):
        for col in range(3):
            if board[box_row + row][box_col + col] == num:
                return False
    
    return True

def solve(board) -> bool:
    for curr_row in range(9):
        for curr_col in range(9):
            if board[curr_row][curr_col] == 0:
                for num in range(1, 10): # 들어갈 수 있는 수 찾기
                    if check(board, curr_row, curr_col, num):
                        board[curr_row][curr_col] = num
                        # 현재 숫자를 채운 상태로 나머지 칸도 풀 수 있는지?
                        if solve(board):
                            return True
                    board[curr_row][curr_col] = 0
                # 1~9까지 어떤 숫자도 채울 수 없을 경우, 실패한 분기(백트래킹)
                return False
    return True

solve(board)

for row in board:
    print(' '.join(map(str, row)))
