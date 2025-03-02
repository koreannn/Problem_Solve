T = int(input())
answer = []

for _ in range(T):
    ox_result = input()
    add_point = 1
    total_point = 0
    
    for char in ox_result:
        if char == 'O':
            total_point += add_point
            add_point += 1
        else:
            add_point = 1
            
    answer.append(total_point)

for p in answer:
    print(p)