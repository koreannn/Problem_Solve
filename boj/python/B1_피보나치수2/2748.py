import sys
input = sys.stdin.readline

n = int(input())

fibo_list = [0]*(n+1)

fibo_list[0] = 0
fibo_list[1] = 1

for i in range(2, n+1):
    fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    
print(fibo_list[n])