N, M = map(int, input().split())
answer_list = []
count = 0

N_set = set()
M_list = []

for _ in range(N):
    N_set.add(input())

for _ in range(M):
    M_list.append(input())

for i in range(len(M_list)):
    if M_list[i] in N_set:
        answer_list.append(M_list[i])
        count+=1

answer_list.sort()
print(count)
for i in range(count):
    print(answer_list[i])