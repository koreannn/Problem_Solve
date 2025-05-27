n = int(input()) # 단어의 개수
words = set(input() for _ in range(n))
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)