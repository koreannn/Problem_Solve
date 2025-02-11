T = int(input())
answer = [0]*T

for l in range(T):
    n = int(input())
    val_list = [0]*n
    if n < 2:
        val_list[0] = 1
    elif n >= 2 and n < 3:
        val_list[0], val_list[1] = 1, 1
    elif n >= 3 and n < 4:
        val_list[0], val_list[1], val_list[2] = 1, 1, 1
    else: # T가 4이상인 경우
        val_list[0], val_list[1], val_list[2] = 1, 1, 1
        for i in range(3, n):
            val_list[i] = val_list[i-2] + val_list[i-3]
    answer[l] = val_list[n-1]

for ans in answer:
    print(ans)