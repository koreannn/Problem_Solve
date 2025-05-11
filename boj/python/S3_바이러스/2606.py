answer = set()

num_of_com = int(input())
connected_num = int(input())
connected_info = {}

for i in range(connected_num):
    key, val = map(int, input().split())
    if key not in connected_info:
        connected_info[key] = [val]
    else:
        connected_info[key].append(val)
    
    # 양방향 연결
    if val not in connected_info:
        connected_info[val] = [key]
    else:
        connected_info[val].append(key)

def dfs(node):
    if node in answer:
        return
    answer.add(node)
    for neighbor in connected_info.get(node, []):
        dfs(neighbor)

dfs(1)
# 정답
print(len(answer)-1)
