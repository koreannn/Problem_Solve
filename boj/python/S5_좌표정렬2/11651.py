N = int(input())
x_y_list = []

for _ in range(N):
    x, y = map(int, input().split())
    x_y_list.append((x,y))

x_y_list.sort(key=lambda point: (point[1], point[0]))

for x, y in x_y_list:
    print(x, y)
