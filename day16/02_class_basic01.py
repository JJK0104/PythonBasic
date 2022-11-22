'''
우리가 지금까지 해 왔던 코딩 방식은 절차지향, 함수지향 프로그램 방식이다
코드를 절차대로

객체 지향은 물건을 만들 때 
코드 뭉태기를 함수로 만들고 함수 조차도 뭉태기로 묶어야 할 때가 있다
함수들을 설계도 안에 넣는 거. 설계도를 하나만 작성하고 공장에서 물건 찍어내듯이 찍어내자
이 때 장점은 효율성
'''
result1 = 0

def add1(n):
    global result1
    result1 += n

def sub1(n):
    global result1 
    result1 -= n

result2 = 0

def add2(n):
    global result2
    result2 += n

def sub2(n):
    global result2
    result2 -= n


add1(8) # result1 = 8
add1(19) # result1 = 27
sub1(15) # result1 = 12

add2(25) # result2 = 25
sub2(12) # result2 = 13

add1(10) # result1 = 22

print("1번 계산기 계산결과: %d" % result1) # 1번 계산기 계산결과: 22
print("2번 계산기 계산결과: %d" % result2) # 2번 계산기 계산결과: 13
 
  
# 계산기가 300개 필요하면 어떻게 할까?

