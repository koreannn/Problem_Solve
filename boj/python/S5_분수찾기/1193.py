x = int(input())
# fractions = ['0']*x
# start_check = False # True일 경우, 짝수번쨰 / False일 경우 홀수번째
# curr_sum = 2
n = 0
total = 0


while total < x:
    n+=1
    total += n
    
prev_total = total - n
pos = x - prev_total

if n%2 == 0:
    num = pos
    den = n - pos + 1
else:
    num = n - pos + 1
    den = pos


# goal = 1
# curr_sum = 2
# start_check = False # True일 경우, 짝수번쨰 / False일 경우 홀수번째
# count = 0

# while count < x:
#     check = 1
    
#     for j in range(count, goal):
#         if start_check: # 짝수번쨰일 경우
#             fractions[j] = f"{check}/{curr_sum - check}"
#         else: # 홀수번쨰일 경우
#             fractions[j] = f"{curr_sum - check}/{check}"
#         check+=1
    
#     count += 1
#     curr_sum += 1
#     goal += 1
#     start_check *= -1
    
# print(fractions[x-1])

"""
1/1
1/2 2/1
3/1 2/2 1/3
1/4 2/3 3/2 4/1

"""