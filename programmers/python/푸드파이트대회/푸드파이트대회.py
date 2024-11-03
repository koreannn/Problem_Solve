def solution(food):
    answer = []
    food_length = 0
    front_idx = 0
    back_idx = 0
    
    for i in range(len(food)):
        food_length += food[i]//2
    
    food_length = food_length*2 + 1
    answer = [0]*food_length

    for i in range(len(food)-1, 0, -1): # 3,2,1
        for l in range(food[i]//2):
            answer[food_length//2-front_idx-1] = i
            front_idx += 1
            answer[food_length//2+back_idx+1] = i
            back_idx += 1
        
    answer = ''.join(map(str, answer))
    return answer

# test case
print(solution([1,3,4,6])) # 각각 0,1,2,3의 개수를 의미 >> food_length = (1+2+3)*2 +1 = 13 > 13//2 = 6 : 가운데(물) 인덱스값
print(solution([1,7,1,2]))
