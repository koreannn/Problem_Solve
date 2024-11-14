def solution(s):
    num_dict = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    answer = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            answer.append(s[i])
            i += 1
        else:
            for word in num_dict:
                if s[i:i+len(word)] == word:
                    answer.append(num_dict[word])
                    i += len(word)
    return int(''.join(answer))

# test
print(solution("1zero"))
print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))

