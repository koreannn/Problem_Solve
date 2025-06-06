words = [input() for _ in range(5)] # 5개의 단어
answer = []

max_len = max(len(s) for s in words)

for i in range(max_len):
    result = ''
    for word in words:
        if i < len(word):
            result+=word[i]
    answer.append(result)

print(''.join(answer))
