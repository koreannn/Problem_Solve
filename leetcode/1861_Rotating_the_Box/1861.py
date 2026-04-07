class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        box_grid_row_len = len(boxGrid)
        box_grid_col_len = len(boxGrid[0])
        rotated_box_grid = [[0] * box_grid_row_len for _ in range(box_grid_col_len)]
        
        for curr_row in range(box_grid_row_len - 1, -1, -1):
            for curr_col in range(box_grid_col_len):
                # rotated_box_grid[curr_col][curr_row] = boxGrid[curr_row][curr_col]
                rotated_box_grid[curr_col][box_grid_row_len - 1 - curr_row] = boxGrid[curr_row][curr_col]
        
        # 뒤집힌 격자의 탐색
        rotated_box_row_len = len(rotated_box_grid)
        rotated_box_col_len = len(rotated_box_grid[0])
        
        # for curr_row in range(rotated_box_row_len - 2, -1, -1): # 아래에 있는 행의 돌부터 먼저 떨궈야함 & 맨 아래 행은 제외
        #     for curr_col in range(rotated_box_col_len):
        #         if rotated_box_grid[curr_row][curr_col] == "#" and rotated_box_grid[curr_row + 1][curr_col] == ".":
        #             tmp = rotated_box_grid[curr_row + 1][curr_col]
        #             rotated_box_grid[curr_row + 1][curr_col] = rotated_box_grid[curr_row][curr_col]
        #             rotated_box_grid[curr_row][curr_col] = tmp
        for curr_row in range(rotated_box_row_len - 2, -1, -1): # 아래에 있는 행의 돌부터 먼저 떨궈야함 & 맨 아래 행은 제외
            for curr_col in range(rotated_box_col_len):
                if rotated_box_grid[curr_row][curr_col] == "#":
                    target_row = curr_row # 내려갈 수 있는 가장 아래 위치 찾기
                    while target_row + 1 < rotated_box_row_len and rotated_box_grid[target_row + 1][curr_col] == ".":
                        target_row
                    
                    rotated_box_grid[target_row][curr_col] = "#"
                    rotated_box_grid[curr_row][curr_col] = "."
        
        return rotated_box_grid

print(Solution().rotateTheBox([["#",".","#"]]))
print(Solution().rotateTheBox([["#",".","*","."],
              ["#","#","*","."]]))