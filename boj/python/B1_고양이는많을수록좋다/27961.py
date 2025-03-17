"""
마법1. 고양이 1마리 생성
마법2. 고양이 일부 또는 전부를 복제 (e.g. 현재 k마리가 존재 -> 0부터 k까지의 마리를 복제할 수 있음)
똑같음
"""

N = int(input())
action_count = 1
curr = 1 # 일단 생성 마법 한번은 쓰고 시작해야함

while True:
    if N == 1:
        break
    
    if N-curr > curr:
        N -= curr
        curr *= 2
        action_count += 1
    else:
        action_count += 1
        break
        
print(action_count)