"""
1/1
1/2 2/1
3/1 2/2 1/3
1/4 2/3 3/2 4/1
...
"""

n = int(input())

count = 1
finded = False
curr_count = 1
numerator = 0
denominator = 0

while True:
    total = curr_count + 1
    if curr_count % 2 == 0: # 짝수번째
        numerator = 1
    else: # 홀수번째
        denominator = 1
    
    for _ in range(curr_count):
        if curr_count % 2 == 0: # 짝수번째 대각선일 경우
            denominator = total - numerator
            
            if count == n:
                finded = True
                break
            
            numerator += 1
        else: # 홀수번째 대각선일 경우
            numerator = total - denominator
            
            if count == n:
                finded = True
                break
            
            denominator += 1
        
        count += 1
    
    curr_count += 1
    
    if finded:
        answer = f"{numerator}/{denominator}"
        break
        
print(answer)


"""
교훈
- 조건에 따라 구현만 잘 하면 되는 문제
- 반복문이 적용되는 범위에 따라 변수 선언 및 초기화에 유의
"""