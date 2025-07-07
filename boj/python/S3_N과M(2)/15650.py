n, m = map(int, input().split())
answers = []

def dfs(start: int, iter_count: int):
    if iter_count == m:
        print(' '.join(map(str, answers)))
        return
        
    for num in range(start, n+1):
        answers.append(num)
        dfs(num+1, iter_count+1) # 다음 숫자부터 시작하면 이미 방문한 숫자는 포함되지x
        answers.pop()
    
dfs(1, 0)