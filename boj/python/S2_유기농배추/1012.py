T = int(input())
answers = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs_search(curr_x, curr_y, curr_cabage_positions):
    curr_cabage_positions.remove((curr_x, curr_y))
    
    for i in range(4): # 네 방향(상, 하, 좌, 우) 탐색
        next_x, next_y = x + dx[i], y + dy[i]
        
        if (next_x, next_y) in curr_cabage_positions:
            dfs_search(next_x, next_y, curr_cabage_positions)

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage_positions = set()
    
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage_positions.add((x, y))
        
    curr_answer = 0 # 현재 테스트케이스의 정답(벌레 수)
    while cabbage_positions:
        x, y = next(iter(cabbage_positions))
        dfs_search(x, y, cabbage_positions)
        curr_answer += 1
    
    answers.append(str(curr_answer))

print('\n'.join(answers))



# def search(curr_x, curr_y, curr_cabbage_positions, curr_answer = 0) -> int: # 현재 탐색 대상의 x, y좌표 / 탐색한 대상을 제외한 나머지의 리스트 / 필요한 지렁이 마리수
#     curr_cabbage_positions.remove((curr_x, curr_y))
    
#     while curr_cabbage_positions:
#         for i in range(len(dx)):
#             if (curr_x + dx[i], curr_y + dy[i]) in curr_cabbage_positions:
#                 curr_cabbage_positions.remove((curr_x + dx[i], curr_y + dy[i]))
#                 search(curr_x + dx[i], curr_y + dy[i], curr_cabbage_positions)
#             else:
#                 curr_answer += 1
#     return

# for _ in range(T):
#     answer = 0
#     M, N, K = map(int, input().split()) # 가로 길이, 세로 길이, 배추 개수(배추가 심어진 위치의 개수)
#     cabbage_positions = set() # 배추가 심어진 좌표 모음
#     for _ in range(K):
#         x, y = map(int, input().split())
#         cabbage_positions.add((x, y))
    
#     initial_position = next(iter(cabbage_positions))
#     answers.append(str(search(initial_position[0], initial_position[1], cabbage_positions, answer)))

# print('\n'.join(answers))