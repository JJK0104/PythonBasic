'''
* 지역변수 (local variable)

- 지역변수란 함수 내부에 선언(생성)된 변수를 말합니다.

- 지역변수는 함수 내부에서만 작동하며 함수가 종료되는 순간
  메모리에서 자동 소멸합니다.
'''
def info():
    word = '안녕' # 지역 변수 : 변수를 만든 위치가 함수 내부
    print(word)

word = info() #info 함수는 return 값이 없다. 
print(word) #word에 저장된 값이 없다 -> None

print("-"*40)

def info2():
    word2 = '안녕'
    print(word2)
    return word2

a = info2()

# print(word2) word2라는 변수가 없다고 오류가 뜬다. 25번째 줄에서 a=info2()에서 word2는 함수가 종료되는 순간 없어짐
print(a)



# 지역 변수의 사용을 함수 내부로 제한하는 이유는
# 변수의 이름 충돌을 피하고 메모리를 절약하기 위함입니다.
print("-" * 40)

def food():
    name = '육개장'
    print(name)

def user():
    name = '홍길동'
    print(name)

food()
user()
food()
user()









