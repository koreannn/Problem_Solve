n, m = map(int, input().split()) # n개중에 m개 뽑기
visited = [False]*(n+1)
answers = []

def dfs(iteration_count: int):
    if iteration_count == m:
        print(' '.join(map(str, answers)))
        return
    for num in range(1, n+1):
        if not visited[num]:
            visited[num] = True
            answers.append(num)
            dfs(iteration_count + 1)
            
            answers.pop()
            visited[num] = False

dfs(0)