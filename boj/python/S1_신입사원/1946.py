# 모든 사람과 비교해봤을 떄, 두 점수 중 하나 이상은 비교대상보다 높아야함
# 서류나 면접 순위 둘 중 하나를 기준 잡고 일단 정렬시켜야함
# 예를 들어, 서류 순위를 기준으로 정렬시킨다면, 정렬시키고나서 앞선 사람들보다 면접 순위에서는 더 높아야함.
T = int(input()) # 테스트 케이스의 수
answer_list = []

for _ in range(T): # 테스트 케이스 수만큼 반복
    N = int(input())
    answer = 1 # 면접 순위가 가장 높은 사람이라면 일단 합격시켜야하므로
    rank_list = [tuple(map(int, input().split())) for _ in range(N)]
    rank_list.sort(key=lambda x: x[0]) # 서류 순위 기준으로 정렬
    
    high_rank = rank_list[0][1] # 서류 1등 기준으로, 서류 2등부터는 면접 점수가 앞선 사람보단 높아야 합격
    for rank in rank_list: # 이후 사람들은, 적어도 면접 순위에서는 더 높아야함.
        if rank[1] < high_rank: # 면접 순위가 더 높다면
            high_rank = rank[1] # 더 높은 면접 순위 갱신
            answer += 1 # 면접 순위가 더 높다면, 이 사람은 합격
        else:
            continue
    
    answer_list.append(answer)
    
for ans in answer_list:
    print(ans)

