from collections import Counter

N = int(input()) # 숫자들의 개수
nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)
sorted_nums = sorted(nums)
list_length = len(nums)

mean = round(sum(nums) // N)
mid = sorted_nums[list_length // 2]
most_freq = Counter(nums)

if list_length == 1:
    if list_length[0] > 0:
        rg = nums[0]
    else:
        rg = -nums[0]
else:
    rg = sorted_nums[-1] - sorted_nums[0]


print(mean)
print(mid)
print(most_freq.values()[0])
print(rg)