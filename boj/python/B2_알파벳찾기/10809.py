S = input()
answer = ['-1']*26 # a가 처음 등장하는 위치 .. z가 처음 등장하는 위치 (값)
pos = 0

for char in S:    
    # i = char가 abcd..z 중 몇 번째 알파벳인지 에서 "몇 번쨰"의 값
    i = ord(char) - 97
    if answer[i] == '-1':
        answer[i] = str(pos)
    
    pos+=1
    
print(' '.join(answer))

