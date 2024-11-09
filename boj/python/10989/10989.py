import sys

n = int(sys.stdin.readline())
count = [0]*10001

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1
    
for idx in range(len(count)):
    if count[idx] != 0:
        for _ in range(count[idx]):
            print(idx)