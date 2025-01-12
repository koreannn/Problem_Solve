answer = 0
N = int(input())
num_list = list(map(int, input().split()))

for num in num_list:
    div_count = 0
    for i in range(1, num):
        if num%i == 0:
            div_count+=1
        if div_count == 2:
            break
        if i==num-1:
            answer+=1
print(answer)