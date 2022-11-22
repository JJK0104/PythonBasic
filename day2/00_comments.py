
'''
파이썬의 주석은 샵기호로 처리합니다.
코드에 추가적인 설명이 필요할 때 주석을 사용합니다.
샵 이후부터 한줄이 전부 주석으로 간주되며
파이썬 인터프리터는 주석을 코드로 인식하지 않습니다.

ctrl + / 을 누르면 한번에 주석처리됨

alt + shift 키 동시에 누르고 아래로 드래그하면 한번에 들여쓰기 쉽게 할 수 있다.

'''

a = 1
b = 2
c = 3

print(a + b + c) # 이 코드는 1+2+3의 결과를 출력하는 문장입니다.

# 실행 단축키는 Ctrl + F5입니다. (이클립스에서는 Ctrl + F11)
print("안녕안녕")
# print("잘가잘가") # Ctrl + / : 빠른 주석처리
print("메롱메롱")

'''
 여러 줄 주석은 삼중따옴표로 처리합니다.
 이 안에 갇힌 모든 내용들은 일괄적으로
 주석처럼 간주됩니다.
'''

# 파이썬에서는 불필요한 들여쓰기 공백은 에러를 유발함.
#      print("헬로!!") (X)

# 파이썬에서는 문장의 끝에 세미콜론을 사용할 수는 있지만
# 권장하지는 않습니다.
# print 2개를 한줄에 쓸 때는 세미콜론을 써줘야한다
print(1 + 3); print(2 + 4) # 4가 출력되고 다음줄에 6이 출력된다

# 파이썬의 모든 명령은 대/소문자를 구분합니다.
# PRINT("안녕") (x)



print("hello~~python!!")
print("hello""hello") # hellohello
print("hello"    "hello") # hellohello
print("hello","hello",'hello') # hello hello hello

# print는 디폴트로 print(sep=" ",end="\n")이 있는거다

print("=======.format 사용법======")
print("{}입니다".format("김정준"))
print("{}은 숫자입니다".format(3))


