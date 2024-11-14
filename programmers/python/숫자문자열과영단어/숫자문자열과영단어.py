def solution(s):
    answer = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            answer.append(s[i])
            i += 1
        elif s[i:i+4] == 'zero':
            answer.append('0')
            i += 4
        elif s[i:i+3] == 'one':
            answer.append('1')
            i += 3
        elif s[i:i+3] == 'two':
            answer.append('2')
            i += 3
        elif s[i:i+5] == 'three':
            answer.append('3')
            i += 5
        elif s[i:i+4] == 'four':
            answer.append('4')
            i += 4
        elif s[i:i+4] == 'five':
            answer.append('5')
            i += 4
        elif s[i:i+3] == 'six':
            answer.append('6')
            i += 3
        elif s[i:i+5] == 'seven':
            answer.append('7')
            i += 5
        elif s[i:i+5] == 'eight':
            answer.append('8')
            i += 5
        elif s[i:i+4] == 'nine':
            answer.append('9')
            i += 4
        else:
            i += 1
    return int(''.join(answer))

# test
print(solution("1zero"))
print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))

