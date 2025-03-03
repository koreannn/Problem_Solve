# def fac(num):
#     if num==1:
#         return 1
#     return num*fac(num-1)

N = int(input())
count = 0

# str_factorial = str(fac(N))

# for i in range(len(str(str_factorial))-1, -1, -1):
#     if str(str_factorial)[i] != '0':
#         break
#     count+=1
for i in range(1, N+1):
    if i%5 == 0:
        count+=1
    if i%25 == 0: # elif로 하면 안됨~
        count+=1
    if i%125 == 0:
        count+=1
    
print(count)