n = int(input())
answer = 0

for _ in range(n):
    word = input()
    word_set = set(list((word)))
    check = True
    is_checked_char = set()
    
    for i in range(len(word)):
        
        changed = False
        
        if i==0:
            is_checked_char.add(word[i])
            continue
        if word[i] != word[i-1]:
            if word[i] in is_checked_char:
                check = False
                break
            is_checked_char.add(word[i])
        
    if check:
        answer += 1

print(answer)