# def is_pair(bracket: str, curr_char:str) -> None : 
def is_pair(bracket: str, curr_char: str) -> bool:
    # if bracket == '[':
    #     if curr_char == ']':
    #         return True
    #     else:
    #         return False
    # else:
    #     if curr_char == ')':
    #         return True
    #     else:
    #         return False
    if bracket == '[':
        return curr_char == ']' # 페어가 맞으면 True, 아니면 False 반환
    else:
        return curr_char == ')'
    
sentence_list = []
while True:
    sentence = input()
    if sentence == '.':
        break
    
    sentence_list.append(sentence)

answer = []

'''
([]) -> yes
([)] -> no
가장 마지막에 들어온거부터 닫아줘함
'''
for sent in sentence_list:
    check_stack = []
    is_balanced = True
    
    # for char in sent:
    #     if char=='(' or char=='[':
    #         check_stack.append(char)
        
    #     if len(check_stack) != 0:
    #         if is_pair(check_stack[-1], char):
    #             check_stack.pop()
    
    # if len(check_stack) != 0:
    #     answer.append("no")
    # else:
    #     answer.append("yes")
    for char in sent:
        if char=='(' or char=='[':
                check_stack.append(char)
        elif char == ')' or char == ']':
            if not check_stack: # 열린괄호 없이 닫는 괄호 먼저 들어온 경우
                is_balanced = False
                break
            if not is_pair(check_stack.pop(), char): # 열->닫 맞게 들어왔어도, 페어가 맞지 않으면
                is_balanced = False
                break
        
    if is_balanced and not check_stack: 
        answer.append("yes")
    else:
        answer.append("no") # 1. 닫힌괄호만 들어왔거나, 2. 페어가 모두 제거되지않고 남아있거나

print('\n'.join(answer))