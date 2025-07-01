t = int(input())
nums = list(map(int, input().split()))

for _ in range(t):
    num = int(input())
    answer = []
    curr_idx = 0
    
    while num > 0:
        if num%2 == 1:
            answer.append(curr_idx)
        num = num//2
        curr_idx+=1
    
print(' '.join(map(str, answer)))

