while(True):
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break
    
    nums.sort()
    if nums[0]**2 + nums[1]**2 == nums[-1]**2:
        print("right")
    else:
        print("wrong")

# while(True):
#     a, b, c = map(int, input().split())
#     if a==0 or b==0 or c==0:
#         break
#     num_list = []

#     num_list.append(a)
#     num_list.append(b)
#     num_list.append(c)

#     sorted_num_list = sorted(num_list)
#     if sorted_num_list[0]**2 + sorted_num_list[1]**2 == sorted_num_list[-1]**2:
#         print("right")
#     else:
#         print("wrong")

