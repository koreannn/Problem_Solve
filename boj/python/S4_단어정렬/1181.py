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

# for i in range(N):
#     for j in range(i+1, N):
#         if len(word_list[i]) > len(word_list[j]):
#             tmp = word_list[i]
#             word_list[i] = word_list[j]
#             word_list[j] = tmp

