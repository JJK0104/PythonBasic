'''
* 정수형(Integer)

- 수치형 타입 중에 정수형(int)은 양수, 음수의 정수값을
  표현하며 소수점 이하 자리는 표현할 수 없습니다.

- 다른 언어는 정수의 저장 범위가 정해져있지만 파이썬은 메모리가
  허용하는 대로 무수히 많은 정수값을 저장할 수 있습니다.
'''
a = 1234
# 변수의 자료형을 확인하는 함수 type()
print(type(a)) # <class 'int'>

b = -4321
print(type(b)) # <class 'int'>

# 파이썬은 10진수 이외에도 2, 8, 16진수를 저장할 수 있습니다.

# 2진수 저장시에는 숫자상수 앞에 접두어 0b를 붙임.
c = 0b1011
print(c)  # 10진수 : 8+0+2+1=11

# 8진수 저장시에는 숫자상수 앞에 접두어 0o를 붙임.
d = 0o77
print(d) # 10진수 : 8*7 + 7 = 63

# 16진수 저장시에는 숫자상수 앞에 접두어 0x를 붙임.
e = 0xac00
print(e) # 10진수 : 10*16^3 + 12*16^2 + 0*16 + 0*1 = 44032

# 정수를 다른 진법으로 출력하려면 아래의 함수를 이용.
print("-----------------------")
print(bin(33))  #2진수로 출력
print(bin(0b100001))  #2진수로 출력
print(oct(0b111001))  #8진수로 출력
print(hex(8923))  #16진수로 출력 




