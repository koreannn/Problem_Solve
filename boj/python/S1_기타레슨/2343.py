'''
블루 레이 > N개의 강의 들어감. 순서 바뀌면 안됨(e.g. i, j번 강의가 블루레이에 포함된다면, i~j사이의 모든 강의가 순서대로 포함되어야함)
N : 강의 개수, M : 가지고있는 블루 레이의 개수
단, 블루 레이의 크기를 최소화하려고 함 -> 블루레이 하나에 포함되는 강의 길이를 최소화 & M개의 블루레이 크기는 다 동일하게 된다 (e.g. 15, 16, 17로 구분되었다면, 17짜리 블루레이로 통일하게됨)

생각한 풀이 방향:
1. 예를 들어, M=3이라고 하면 전체 강의를 삼등분 해야함 -> 막대 2개를 중간에 끼워넣는다고 생각. 단, 막대의 위치는 시작점, 끝점은 안되고, 막대가 중첩되는 경우가 없어야함
2. 리스트 내의 숫자 중 가장 큰 수를 최솟값으로 정해두고, 점차 값을 크게해가는 방식
'''

N, M = map(int, input().split())
lecture_time_list = list(map(int, input().split()))
min_time_sum = max(lecture_time_list)
max_time_sum = sum(lecture_time_list)

# 값 찾는 알고리즘 -> 이진탐색
result = max_time_sum

while(min_time_sum <= max_time_sum):
    mid = (min_time_sum + max_time_sum) // 2
    num_of_blue = 1
    time_of_curr_blue = 0
    
    for time in lecture_time_list:
        if time_of_curr_blue + time > mid: # 현재 블루레이에 시간을 더 못담을 경우
            num_of_blue += 1 # 새로운 블루레이를 추가
            time_of_curr_blue = time # 새로운 강의를 다음 블루레이 타임에 추가
        else:
            time_of_curr_blue += time # 현재 블루레이에 추가
    
    # 블루레이 개수가 M개인지 확인
    if num_of_blue <= M: # 가능할 경우
        result = mid 
        max_time_sum = mid-1 # 더 작은 값 찾아보기
    else: # 불가능할 경우
        min_time_sum = mid+1 # 더 큰 값으로 다시 찾아보기

print(result)