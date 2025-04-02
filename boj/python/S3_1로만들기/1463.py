n = int(input())
counts = [0]*1000001

counts[1] = 0
counts[2] = 1
counts[3] = 1

for i in range(4, len(counts)):
    curr = i
    min_val = counts[curr-1] # 1을 뺴는 경우부터 고려해주기
    
    if curr % 2 == 0:
        min_val = min(min_val, counts[curr//2])
    
    if curr % 3 == 0:
        min_val = min(min_val, counts[curr//3])
    
    counts[curr] = min_val + 1 # 마지막에 1 더하기(1을 뺴거나, 2로 나누거나, 3으로 나누거나)

print(counts[n])