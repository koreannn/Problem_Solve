heights = [int(input()) for _ in range(9)]
sorted_heights = sorted(heights)
check = False
height1 = 0
height2 = 0

for i in range(len(sorted_heights)-1, -1, -1):
    heights_sum = sum(sorted_heights)
    height1 = sorted_heights[i]
    heights_sum = heights_sum - height1
    for j in range(i, -1, -1):
        height2 = sorted_heights[j]
        if (heights_sum - height2) < 100:
            continue
        if (heights_sum - height2) == 100:
            check = True
            break
        
    if check:
        break

for h in sorted_heights:
    if (h == height1) or (h == height2):
        continue
    print(h)