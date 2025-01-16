# N = int(input())
# people_dict = {}

# for _ in range(N):
#     age, name = input().split()
#     people_dict[age] = name

# sorted_dict = sorted(people_dict.items(), key=lambda x: x[0])

# for i in range(N):
#     print(sorted_dict[i][0], sorted_dict[i][1])

N = int(input())
# people_list = [[]]
people_list = []

for i in range(N):
    age, name = input().split()
    people_list.append((int(age), name))
    # people_list[i].append(age)
    # people_list[i].append(name)

sorted_list = sorted(people_list, key=lambda x: x[0])

for age, name in sorted_list:
    print(age, name)
