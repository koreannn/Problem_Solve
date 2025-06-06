words = [input() for _ in range(5)]
answer = ''

max_length = len(max(words, key=lambda x:len(x)))

for l in range(max_length):
    for i in range(5):
        if words[i] != "":
            answer += words[i][0]
            words[i] = words[i][1:]
        else:
            continue

print(answer)