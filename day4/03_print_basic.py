

'''
* 표준 출력함수 print()

- 파이썬의 표준출력함수는 print이고 괄호 안에 출력하고 싶은
  변수, 상수, 수식 등을 적으면 콘솔창에 텍스트 출력을 실행합니다.
'''
value = 1234
name = "신사임당"

print(value)
print(name)
print(5678)
print("홍길동")
print(value * 3) #수식을 넣어도 됨

'''
- 출력할 데이터 여러 개라면 괄호 안에 출력할 데이터들을 콤마(,)로
  나열하여 작성합니다.

- 이 때 여러 개의 값들을 공백과 함께 가로로 나란히 출력합니다.
'''
dog = "멍멍이"
cat = "야옹이"
print(dog, cat) # 멍멍이 야옹이
print(dog,             cat) # 멍멍이 야옹이
print(dog, cat, 23) # = print(dog, cat, 23, sep = " ") 멍멍이 야옹이 23

'''
- print함수 내부에는 sep이라는 속성이 존재하고 있습니다.
- sep은 separator의 약자로 구분자라고 불립니다.
- sep의 값은 디폴트로 " " 공백 문자열이 지정되어 있습니다.
'''
print("-" * 40)
print(dog, cat, 23, sep=" ")
print(dog, cat, 23, sep=",")
print(dog, cat, 23, sep="=>") # 멍멍이=>야옹이=>23
print(dog, cat, 23, sep="")

print("-" * 40)
f1 = "닭강정"
f2 = "김말이"
f3 = "볶음밥"
f4 = "짜장면"

# sep속성을 이용하여 '닭강정 먹고 김말이 먹고
# 볶음밥 먹고 짜장면'을 하나의 print로 출력하세요.
print(f1, f2, f3, f4, sep=" 먹고 ")

'''
- 파이썬의 print함수가 자동으로 줄개행을 하는 이유는
  함수 내부에 end라는 속성값이 지정되어 있으며 디폴트로
  "\n"이 정해져있기 때문입니다.

print는 디폴트로 print(sep=" ",end="\n")이 있는거다
'''
print("hello") ; print("world")
# hello
# world

print("-" * 40)
print(dog, end="\n")
print(cat, end="\n")

print(dog, end="랑 ")
print(cat, sep=" ", end="\n")

print("안녕","잘가", end="\n", sep=" ") # (O)
# print(end="\n", sep=" ", dog, "헬로") (X) 
# end, sep 순서는 상관 없지만 맨 뒤에 있어야 된다.


# 멍멍이와 야옹이 신난다!!
print(dog, end="와 ")
print(cat, end=" ")
print("신난다!!")

# 김밥!!단무지!!볶음밥==>마시썽~~ㅠㅠ
gim = "김밥"
dan = "단무지"
bob = "볶음밥"
print(gim, dan, bob, sep="!!", end="==>")
print("마시썽~~ㅠㅠ")







