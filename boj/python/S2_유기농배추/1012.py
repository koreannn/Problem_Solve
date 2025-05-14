T = int(input())
answer_list = []
# 접한다 = x좌표 또는 y좌표값 둘 중 하나만 1 차이가 난다.

for test_num in range(T):
    M, N, K = map(int, input().split()) # 가로 길이, 세로 길이, 배추가 심어져있는 위치의 개수
    point_list = [] # 배추 위치 좌표값 모음
    answer = 0 # 필요한 지렁이 마리 수
    
    for i in range(K): # 배추의 위치(좌표)
        x, y = map(int, input().split())
        point_list.append((x, y))

    if len(point_list) != 0:
        answer = 1
        curr = point_list[0][0] +  point_list[0][1] # 기준점
        point_list.sort(key=lambda iter: iter[0]) # x좌표 기준 정렬


    for i in range(1, len(point_list)):
        if (abs(curr - point_list[i][0] + point_list[i][1])) == 1:
            curr = point_list[i][0] + point_list[i][1]
        else:
            answer += 1
            curr = point_list[i][0] + point_list[i][1]
    
    answer_list.append(str(answer))

print(answer_list)