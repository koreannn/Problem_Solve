N = int(input())
word_list = []
tmp = ''

for _ in range(N):
    word = input()
    word_list.append(word)

unique_list = set(word_list)
sorted_word_list = sorted(unique_list, key=lambda x: (len(x), x))

for word in sorted_word_list:
    print(word)



