n = int(input())
count = 0

def fac(num):
    if num==1:
        return 1
    return num*fac(num-1)

factorial = fac(n)

while(True):
    if factorial%10 != 0:
        break
    factorial //= 10
    count+=1
    
print(count)

