A = int(input())
B = int(input())
C = int(input())

num_list = [0]*10 # 0~9의 개수
val = str(A*B*C)

for num in val:
    num_list[int(num)] += 1

for num in num_list:
    print(num)