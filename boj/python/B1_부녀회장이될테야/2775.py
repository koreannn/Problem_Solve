test_case = int(input())

for _ in range(test_case):
    k = int(input()) # 층
    n = int(input()) # 호
    
    apt = [[0]*(n+1) for _ in range(k+1)] # 몇 명 사는지 초기화를 위한 초기 배열
    
    