n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
answer = 0

a_list.sort()
b_index = sorted(range(n), key=lambda i: b_list[i], reverse=True)

for i in range(n):
    answer += a_list[i]*b_list[b_index[i]]

print(answer)