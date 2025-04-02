n, m = map(int, input().split())
n_list = list(map(int, input().split()))
answer = []

for _ in range(m):
    start, end = map(int, input().split())
    
    ans = n_list[start-1]
    ans += sum(n_list[start:end])
        
    answer.append(ans)
    
for num in answer:
    print(num)
