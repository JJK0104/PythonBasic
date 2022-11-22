

'''
* 반환값 (return value)

- 반환값은 함수를 호출한 곳으로 함수의 최종실행 결과를 전달하는 값입니다.

- 인수는 호출부에서 함수에게 전달되는 값이고 반환값은 호출부에 실행결과를
  보고하는 값입니다.

- 인수는 여러 개 존재할 수 있지만 반환값은 언제나 하나만 존재해야 합니다.
  그래서 정수 50개를 갖다 줄려면 리스트에 담아 주면 된다.
  리스트 2개 주고 싶으면 2차원 리스트에 담아서 주면 된다.

- return이라는 키워드를 사용하여 뒤에 전달할 값을 지정합니다.

- 반환값이 있는 함수의 호출문은 그 자체가 하나의 값으로 취급되기 때문에
  반환된 값을 다른 변수에 대입할 수도 있고, 다른 함수의 인수로 사용할 수도
  있습니다.
'''
def add(n1, n2):
    return n1 + n2 

result = add(10, 5) # result = 15 , 대입 연산에서는 우항 연산이 먼저다. add(10,5)가 먼저 실행됨
print(result)

print(add(17, 3), add(3, 5)) # print(20, 8) => 20 8 출력, 실행 순서는 add(17,3)이 먼저 실행되고 add(3,5)이 실행된다

result = add(add(5,7), add(9,8)) #실행 순서는 1)add(5,7) 2)add(9,8) 3)add(add(5,7),add(9,8)) 4)result
print(result)

# n = int(input('정수: ')) # n = int("35"), input이 먼저 실행되고 int가 실행된다

'''
- 모든 함수가 반환값이 반드시 필요한 것은 아닙니다.
- 함수 실행을 후에 딱히 반환할 데이터가 없다면
  return을 사용하지 않아도 됩니다.
'''
def multi(n1, n2):
    result = n1 * n2
    print("%d x %d = %d" % (n1, n2, result))
    

a = multi(3, 8) # multi라는 함수를 만나서 실행한다 
                # print("%d x %d = %d" % (n1, n2, result)) 출력됨
print(a) #None. return 값이 없다

'''
- 위 예제의 multi함수는 곱셈의 값을 구해서 호출부로 전달해주는 게 아니라
  직접 곱셉을 수행하여 결과를 콘솔창에 출력하는 함수입니다.

- 함수 내부에서 모든 로직한 후 반환값이 없기 때문에 return을 사용하지
  않습니다.

- 반환값이 없는 함수는 동작만 처리할 뿐 값이 아니기 때문에 다른 변수에
  대입하거나 수식 내에서 사용할 수 없고 단독으로 호출해서 사용해야 합니다.
'''
print("-" * 40)

print(add(4, 7) * 10) # print(11 * 10)
# print(multi(5, 6) - 13) # print(None - 13) 에러

multi(add(2,4), add(4,8)) # multi(6, 12) 

# add(multi(5,5), 13) (X)

'''
- 함수의 반환값은 오직 하나입니다.

- 다만 파이썬에서는 특별하게 return 키워드 뒤에 반환값을 콤마로
  여러 개 나열할 수 있습니다.

- 이런 경우에는 리턴값이 여러 개가 되는 것이 아니라 해당 값들을 하나의
  튜플로 묶어서 반환합니다.
'''
def sum_multi(n1, n2):
    add_res = add(n1, n2)
    mul_res = n1 * n2
    return add_res, mul_res # 튜플에서 소괄호 생략할 수 있으니까... 생략했다고 보고

x = sum_multi(5, 5)
print(type(x)) # <class 'tuple'>
print(x) # (10,25)
print(x[0], x[1]) # 10 25
print(type(x[0])) # int


'''
- 모든 함수는 함수 정의부에서 return키워드를 만나는 순간 함수가
  강제로 종료됩니다.

- 마치 반복문이 break를 만나면 반복문을 강제로 종료하는 것과
  비슷한 원리입니다.
'''
print("-" * 40)

def sum_sub(n1, n2):
    return n1 + n2 #return 만나는 순간 종료되고 밑에 거는 실행 안된다
    return n1 - n2

print(sum_sub(10, 5))


def say_nickname(nick):
    if nick == "바보":
        print("그런 별명 부르지마~~~!")
        return #반복문의 break처럼 쓴거다
        ㅁㄴㅇㄻㄴㅇㄻㄴㅇㄻㄴㅇㄹ
    print("나의 별명은 %s입니다." % nick)

print("-" * 40) 
n = input("별명: ")
say_nickname(n)





