N = int(input())
time_list = list(map(int, input().split()))
answer = 0

time_list.sort(reverse=True)

for i in range(N, -1, -1):
    answer += time_list[i-1]*i

print(answer)