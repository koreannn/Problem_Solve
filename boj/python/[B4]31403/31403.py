# A, B, C = input().split()
A = input().strip()
B = input().strip()
C = input().strip()

int_answer = int(A)+int(B)-int(C)
str_answer = int(A+B) - int(C)

print(int_answer)
print(str_answer)