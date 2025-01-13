T = int(input())
TRUE = 1
FALSE = 0

for _ in range(T):
    N = int(input()) 
    N_list = set(map(int, input().split())) # 수첩 1에 적힌 숫자들 (정답)
    
    M = int(input()) 
    M_list = list(map(int, input().split())) # 연종이가 말한 숫자들의 arr 

    for num in M_list:
        if num in N_list:
            print(f"{TRUE}")
        else:
            print(f"{FALSE}")
