P = int(input())
answer = []

for _ in range(P):
    answer_string = ''
    iter_count, string = input().split()
    for char in string:
        answer_string += char*int(iter_count)
    answer.append(answer_string)

print('\n'.join(answer))
