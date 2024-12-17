import re

command_count = int(input()) # 1<=N<=10,000
stack = []
answer_list = []

for i in range(command_count):
    command = input()
    if "push" in command:
        element = re.findall(r'\d+', command) # e.g. 123 -> ['1', '2', '3'] 이런식으로 반환함
        element = int(''.join(element))
        stack.append(element)
        # print(f"[Stack] {stack}")
        # print(f"[Pushed] {element}\n")
        
    elif "pop" in command:
        if len(stack)!=0:
            answer = stack.pop()
        else:
            answer = -1
        answer_list.append(answer)
        # print(f"[Stack] {stack}")
        # print(f"[Poped] {answer}")
        
    elif "size" in command:
        answer = len(stack)
        answer_list.append(answer)
        # print(f"[Stack] {stack}")
        # print(f"[Length of Stack] {len(answer_list)}")
        
    elif "empty" in command:
        answer = int(len(stack) == 0) # 비어있다면 1, 아니면 0을 반환
        answer_list.append(answer)
        # print("Stack : ", stack)
        
    else: # top
        if len(stack)!=0:
            answer = stack[-1]
        else:
            answer = -1
        answer_list.append(answer)
        # print("Stack : ", stack)

for ans in answer_list:
    print(ans)

