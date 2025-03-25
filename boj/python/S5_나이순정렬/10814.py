n = int(input())
info = []

for _ in range(n):
    age, name = input().split()
    info.append((age, name))

info.sort(key=lambda information:information[0])

for i in range(n):
    print(info[i][0], info[i][1])