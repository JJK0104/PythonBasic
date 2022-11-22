
# 문자열과 정수의 상호변환

name = "강감찬" #문자열
score = 90 #int

# print(name + "의 점수는: " + score) 문자열과 정수는 더할 수 없다

'''
- 문자열과 정수의 + 연산 진행시 타입이 일치하지 않아서
  에러가 발생하므로 타입을 어느 한쪽으로 맞춰야 합니다.

- 정수를 문자열로 변환할 때는 str()함수를 사용합니다.
'''
print(name + "의 점수는: " + str(score)) # score가 일시적으로 변함 , + 는 띄어쓰기 없이 바로 이어붙인다
print(type(score)) #int

score = str(score) #score가 영원히 str로 바뀜
print(type(score)) #str

n1 = 10
n2 = "34"
print(str(n1) + n2) #44가 아닌 1034가 됨

# 문자열을 정수로 변환할 때는 int()함수를 사용합니다.
print(n1 + int(n2))

# 문자열 내부에 순수한 정수값이 들어있지 않으면 에러가 발생합니다.
# print(n1 + int("20%"))  (X)
# print(int("3.14"))    (X)




