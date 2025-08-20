n, m = map(int, input().split())
answer = 0

s = set() # n개의 문자열 집합 (같은 문자열이 주어지는 경우는 없다고 가정)

for i in range(n):
    curr_input = input()
    s.add(curr_input)
    
for j in range(m):
    curr_test = input()
    if curr_test in s:
        answer += 1
        
print(answer)