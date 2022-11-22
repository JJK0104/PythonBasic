class Calculator: # 도면의 이름을 적어준다 "Calculator"
    
    result = 0
    
    def add(self, n): # self관련된 거는 04_class_basic03에서 배운다. 일단 보기
        self.result += n
    
    def sub(self, n):
        self.result -= n

# 도면을 만들었으면 이제 계산기 만들기

cal1 = Calculator() # 1번 계산기 생성
cal2 = Calculator() # 2번 계산기 생성
cal3 = Calculator() # 3번 계산기 생성

cal1.add(4)
cal1.add(19)
cal1.sub(5)

cal3.add(56)
cal3.sub(27)

print("1번 계산기 계산결과: %d" % cal1.result) # 1번 계산기 계산결과: 18
print("2번 계산기 계산결과: %d" % cal2.result) # 2번 계산기 계산결과: 0
print("3번 계산기 계산결과: %d" % cal3.result) # 3번 계산기 계산결과: 29


print(type([1,2,3])) # <class 'list'>
# 결국에는 얘가 class이기 때문에 ~.해서 어떤 행위들을 독립적으로 하고 있었던 거다
# ex) a = [1,2,3]
#     a.append(2)
'''
파이썬의 기본 자료형은 10개다 int,float,complex,bull,None,str,list,tuple,dictionary,set
근데 파이썬의 자료형은 10개가 아니다. 기본 자료형이 10개인 거지. 기본으로 내장되어 있는 자료형이 10개고
그 이외의 자료형은 내가 class를 통해 직접 만들어낼 수 있다.
그래서 파이썬의 자료형은 무한대이다. 우리가 원하는 만큼 만들 수 있다.
'''
# 자료형은 메모리에 자료를 보관할 때 어떤 형태로 어떤 용량을 할당해서 자리를 잡을 것인가를 정하는 거 

# cal1,cal2,cal3는 변수이다. 대입 연산자를 통해 대입하고 있으니까
# 변수면 다 자료형이 있다
# cal1의 자료형은 Calculator 즉 사용자 정의 자료형이다
# cal1이 Calculator 형태이기 때문에 .add , .sub 메서드를 쓸 수 있는 거다
# list 형태이기 때문에 .append, .insert, .extend 쓸 수 있고, str 형태이기 때문에 .strip, .find 같은 거 쓸 수 있듯이

print(type(cal1)) # <class '__main__.Calculator'> 우리가 만들어낸 main내부의 Calculator 자료형이다
                  # __main__이 붙는 이유는 다른 사람도 Calculator 자료형을 만들 수 있으니 그거랑 구분하기 위해서 '우리' 거라는 
                  # 다른 사람이 만들면 다른 사람 소속 모듈이 나온다. 어떤 모듈의 Calculator인지
                  
print(type(cal2)) # <class '__main__.Calculator'>
print(type(cal3)) # <class '__main__.Calculator'>

print("-"*50)


# 아래는 day 15 <calculator 모듈> 부분
print("__name__의 값:", __name__) # 여기서 출력하면 __name__의 값: __main__ 이 나온다
# 하지만 04_module_basic03 에서 실행하면 __name__의 값: calculator , 모듈의 이름이 나온다
# 따라서 아래 if문은 거짓이 되고 출력 되지 않는다

#  __name__ 변수의 특징은 우리가 실행하고자 하는 모듈 내부에서는 거기에 "__main__"이
# 자동 저장되게 설정되어 있다
# import될 때는 __name__에다 <import 당하는 모듈의 이름>이 저장되게 세팅 돼있다 파이썬 내부적으로 
# 예를 들어 04_module_basic03 에서 import calculator as cal 라고 입력하면 
# print("__name__의 값:",__name__)은 __name__의 값: calculator 라고 출력된다

if __name__ == "__main__": # 실행이 된다 --> 즉 True가 나왔다
    print("__name__ == __main__")


