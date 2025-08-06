string = input()

change_set = set(['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='])

idx, answer = 0, 0

while idx < len(string):
    if string[idx:idx+2] in change_set: # 두 단어의 길이일 경우
        answer += 1
        idx += 2
    elif string[idx:idx+3] == 'dz=': # 세 단어의 길이일 경우('dz='밖에 없긴함)
        answer += 1
        idx += 3
    else: # 없는 단어일 경우
        answer += 1
        idx += 1

print(answer)