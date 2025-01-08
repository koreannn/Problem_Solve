N = int(input())
bulk_list = [tuple(map(int, input().split())) for _ in range(N)]

ranking = [1]*N

for i in range(N):
    for j in range(N):
        if i != j: # 다른 사람에 대해서만~
            if bulk_list[j][0] > bulk_list[i][0] and bulk_list[j][1] > bulk_list[i][1]:
                ranking[i] += 1 # 후순위로 밀어내기

print(' '.join(map(str, ranking)))