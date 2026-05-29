# number(숫자형)
# - 정수
# - 실수
# - 복소수

# type(변수명 | 값) 함수 : 변수 또는 값을 확인하는 내장 함수

# 정수 int (Integer)

print(" --- 정수 --- ")
n = 123
print(n, type(n))

price = 10_000_000_000; # 정수 자릿수 구분
print(price, type(price))

# 정수의 최댓값
import sys
print(sys.maxsize, type(sys.maxsize))

# 2진법, 8진법, 16진법
a = 0b100 # == 4
print(a, type(a))

b = 0o23 # == 19
print(b, type(b))

c = 0xff # == 255
print(c, type(c))

#---------------------------------------
# 실수 (float)

print(" --- 실수 --- ")
f1 = 123.456
print(f1, type(f1))

f2 = -99999.99999
print(f2, type(f2))

f3 = 1.012345678901234567890
print(f3, type(f3)) # 소숫점 아래 16자리까지 표현 가능

#---------------------------------------
# 복소수 (complex)

print(" --- 복소수 --- ")
c = 2j
print(c, type(c))

d = 3 + 4j
print(d, type(d))

#---------------------------------------
# 산술 연산 (+, -, *, /, //, %, **)

print(" --- 산술연산 --- ")
print("더하기",1 + 2) # 3
print("빼기", 1 - 2) # -1
print("곱하기", 1 * 2) # 2
print("나누기", 1 / 2) # 0.5 -> 나누어 떨어질 때까지의 몫
print("몫", 1 // 2) # 0 -> 정수 부분의 몫
print("나머지", 1 % 2) # 1
print("거듭제곱", 2**3) # 8
print("int 양의 최댓값", 2**63)