
'''
* 논리형(boolean)

- 논리형 데이터 타입은 명제가 참일경우 True,
  거짓일 경우 False값을 가집니다.

- 파이썬에서 논리값은 대문자 True, False 밖에 없다

'''
b1 = True
b2 = False
print(type(b1)) # <class 'bool'>

# b3 = true (X) 소문자 true 는 변수다. 
# b4 = "True" (X) ""에 넣으면 문자다
# print(type(b4)) 은 str 문자열이 뜬다

b3 ='a'
print(type(b3)) # <class 'str'>

'''
* 비교 연산자 (==, !=, <, <=, >, >=)
* = 이 다른 기호와 함께 쓰이면 = 은 항상 오른쪽에 쓴다.

- 비교 연산의 결과는 항상 논리값
- 좌항과 우항을 비교하여 논리값을 도출하는 연산자입니다.
'''
a = 5
print(a < 10) # True
print(a >= 10) # False
print(a != 10) # True


# = 은 대입 연산자, ==은 비교 연산자
# = 이라는 대입 연산자는 연산자 중 우선순위가 제일 낮다(,가 제일 낮다)
b = a == 5   #a==5는 True -> b = True -> b는 'bool'
print(type(b)) # <class 'bool'>
'''
C언어에서 연산자 우선순위
1순위) () , [] , -> , . (왼쪽부터 차례대로 우선순위 높다... ()가 1짱)
2순위) 연산자 항의 개수가 적을수록 먼저 실행 ex) !1||0 여기서 !은 단항연산자, ||은 2항연산자
따라서 단항연산자 먼저 실행돼서 !1||0 => 0||0 => 0
3순위) 산술 > 관계 > 논리 > 대입
'''

'''
- 문자열도 동등, 비동등 비교를 할 수 있습니다.
- 단, 대/소문자까지 정확히 일치해야 True를 도출합니다.
'''
print("-------------------")

password = "abc1234"
print(password == "ABC1234")
print(password != "Abc1234")
print(password == "abc1234")

'''
- 문자열도 대/소 비교가 가능합니다.
- 문자열끼리 크기를 비교할 때는 사전 순서대로 비교합니다.
- 사전에 앞에 등장하는 단어를 작다고 봅니다.
- 컴퓨터에서 사용하는 모든 문자 데이터들은 메모리에 저장될 때 정수형태로 저장된다
A : 65, B = 66, C = 67 ...
a : 97, b = 98, c = 99 ...
가 : 44032  
- 대문자 < 소문자 < 한글 

'''
print("------------------")
print("apple" < "grape") #True
print("abc" < "adc") # a는 97로 같지만 b 98 < d 100
print("감자" > "양파") # False
print("peach" < "Zebra") # False





