n, k = map(int, input().split())
n_list = list(range(1, n+1))
count = 0
answer = []
curr_idx = 0

while n_list:    
    if count == k:
        answer.append(n_list.pop(curr_idx))
        count = 0
    count += 1
    curr_idx += 1