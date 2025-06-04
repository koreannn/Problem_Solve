from collections import deque
answer = []

while True:
    string = input()
    if string == '0':
        break
    reverse = deque()
    for i in range(len(string)-1, -1, -1):
        reverse.append(string[i])
    reverse_str = ''.join(reverse)
    
    if string == reverse_str:
        answer.append("yes")
    else:
        answer.append("no")

print("\n".join(answer))