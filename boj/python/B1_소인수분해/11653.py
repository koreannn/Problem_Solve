n = int(input())
i = 2
answer = []

while n!=1:
    if n%i == 0:
        n = n//i
        answer.append(str(i))
        i = 2
    else:
        i += 1
    
print('\n'.join(answer))