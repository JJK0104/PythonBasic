
'''
1. 회원의 이름과 성별 그리고 나이를 입력받으세요.
2. 이름 변수는 name, 성별은 gender, 나이는 age입니다.
3. 입력받은 값을 통해 회원의 이름과 
     성별과 나이와 출생년도를 출력하세요.
'''
name = input("이름: ")
gender = input("성별: ")
age = int(input("나이: "))
birthYear = 2022 - age + 1
print("----------------------")
print("이름:", name) # 디폴트 sep = " "
print("성별:", gender)
print("나이:", age)
print("출생년도:", birthYear)






