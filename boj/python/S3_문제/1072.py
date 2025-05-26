x, y = map(int, input().split()) # 게임 수, 이긴 게임 수 
z = y*100 // x # 승률 (e.g. 게임 판수: 53 / 이긴 게임 수: 47 ==> 47/53 약 88(소숫점 버림))

def get_new_rate(x, y, mid):
    return (y+mid)*100 // (x+mid)

if z >= 99:
    print(-1)
else:
    left = 1
    right = 1_000_000_000
    answer = -1
    
    while left <= right:
        mid = (left + right) // 2
        new_z = get_new_rate(x, y, mid)
        
        if new_z > z: # 더 작은 값이 있는지 탐색
            answer = mid
            right = mid-1
        else:
            left = mid + 1
    
print(answer)