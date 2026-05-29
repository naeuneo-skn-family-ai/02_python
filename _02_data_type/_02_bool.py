# 논리형 Boolean

a = True
b = False
print(a, type(a))
print(b, type(b))

#---------------------------------------
# 비교 연산
# A > B : A가 B보다 크면(초과) True, 아니면 False(이하)
# A >= B : A가 B보다 크거나 같으면(이상) True, 아니면 False(미만)
# A == B : A, B가 같으면 True, 아니면 False
# A != B : A, B가 같지 않으면 True, 아니면 False

print("1 > 0.5:", 1 > 0.5) # T
print("1 < 0.5:", 1 < 0.5) # F
print("1 >= 0.5:", 1 >= 0.5) # T
print("1 <= 0.5:", 1 <= 0.5) # F
print("1 == 1:", 1 == 1) # T
print("1 != 1:", 1 != 1) # F

#---------------------------------------
# 논리 부정 연산 not
print(True)
print(not True)