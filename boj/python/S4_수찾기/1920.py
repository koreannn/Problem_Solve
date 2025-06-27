n = int(input())
ground_truth = sorted(map(int, input().split()))
m = int(input())
query = map(int, input().split())
answer = []

for num in query:
    left, right = 0, n-1
    finded = False
    
    while left<=right:
        mid = (left+right)//2
        
        if num == ground_truth[mid]:
            finded = True
            break
        elif num > ground_truth[mid]:
            left = mid+1
        else:
            right = mid-1
    
    if finded:
        answer.append("1")
    else:
        answer.append("0")
    
print('\n'.join(answer))