
'''
* 다중 예외처리
- 한 개의 try블록에서 발생하는 예외의 원인에 따라 다르게 예외처리를
  하는 방법.

- 자주 발생하는 예외
1. NameError: 정의되지 않은 변수, 함수, 클래스를 사용할 때 발생
2. ValueError: 주로 형 변환 시 내부 값의 형식이 잘못되었을 때 발생
3. ZeroDivisionError: 숫자를 0으로 나눌 경우 발생.
4. IndexError: 문자열이나 리스트 등 시퀀스 데이터의 
  존재하지 않는 인덱스를 참조했을 경우 발생.
5. TypeError: 연산 수행시 데이터의 타입이 일치하지 않을 경우 발생.
'''

# NameError
# print(apple)
# insert()
# stu = Student()

# ValueError
# int("3.14")

# IndexError
s = "hello"
# print(s[6])

# TypeError
# print(10 ** "hello")

print("-" * 40)
s = input('정수: ')
print()


# 작동 원리는 try 내부에서 여러 상황의 예외가 발생했을 때
# try 내부에서 print = int(s)에서 에러가 터진다면 try는 에러가 터지는 순간 try 실행을 중단하고 except를 찾아간다
# except가 여러개 있을 경우에는 제일 위에 있는 애부터 찾아간다 그리고 처리가능하면 아래 except는 실행 X
 
try:
    point = int(s) # ValueError 가능성
    print(150 / point) # ZeroDivisionError 가능성
    a = s[2] # IndexError 가능성
except ValueError:
    print()
    print("*ValueError 발생")
    print("숫자로만 입력하세요~")
except ZeroDivisionError:
    print()
    print("*ZeroDivisionError 발생")
    print("0으로 나눌 수 없습니다.")
except: # 그냥 except를 쓰면 만능이다
        # default except는 마지막에 써야된다. 처음으로 쓰면 에러난다
    print()
    print("*알 수 없는 오류 발생! 점검 후 조치하겠습니다!")

print()
print("프로그램 정상 종료!")






