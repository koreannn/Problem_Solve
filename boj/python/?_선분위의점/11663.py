from bisect import bisect_left, bisect_right

N, M = map(int, input().split()) # 각각 좌표의 개수, 선분의 개수
point_list = list(map(int, input().split()))
point_list.sort()
answer_list = []

for _ in range(M):
    start, end = map(int, input().split())
    left_idx = bisect_left(point_list, start)
    right_idx = bisect_right(point_list, end)
    answer_list.append(right_idx-left_idx)

# for _ in range(M):
#     count = 0
#     start, end = map(int, input().split())
#     for i in range(len(point_list)):
#         mid = len(point_list)//2
        
    # for point in point_list:
    #     if start <= point and end >= point:
    #         count+=1
    # answer_list.append(count)

# for answer in answer_list:
#     print(answer)
print('\n'.join(map(str, answer_list)))
