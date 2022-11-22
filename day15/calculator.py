# 계산 관련된 기능을 calculator.py에 모아 놓으려함


INCH = 2.54

def calc_sum(end):
    sum = 0
    for n in range(end+1):
        sum += n
    return sum

def info():
    print("모듈 임포트!! 연습!") 

# 아래 코드를 쓰고 04_module_basic03을 실행시키면 아래 코드도 출력된다
# ctrl + / = 한번에 주석처리 
print("1~50까지의 누적합:", calc_sum(50)) 
print("메롱메롱")
print()



'''
* 테스트 기록을 남겨야 된다면 

* 테스트 코드 작성법

- 처음부터 import를 목적으로 설계된 모듈의 테스트 코드 작성시에는
  자 이 calculator란 모듈은 코드의 분산 관리 차원에서 그냥 우리가 import를 할려고 그런 목적으로 따로 빼 놓은 거란 
  말이야 코드들을 함수 정의부랑 변수 선언부를 따로 빼놓은 거다. 이런 애들 코드 작성할 때는
  다음과 같은 문법하에서 코드를 작성합니다.


- 앞뒤로 __ 있으면 파이썬 내부에 내장 되어있는 변수다
 
ex) if __name__ == "__main__":
        test code....

- __name__ 변수의 특징은 우리가 실행하고자 하는 모듈 내부에서는 거기에 "__main__"이
자동 저장되게 설정되어 있다
import될 때는 __name__에다 import하는 모듈의 이름이 저장되게 세팅 돼있다 파이썬 내부적으로 

- __name__변수는 실행 중인 모듈의 이름이 저장되는데, 단독
  실행시에는 "__main__"이 저장됩니다.
'''

print("__name__의 값:", __name__) # 여기서 출력하면 __name__의 값: __main__ 이 나온다
# 하지만 04_module_basic03 에서 실행하면 __name__의 값: calculator , 모듈의 이름이 나온다
# 따라서 아래 if문은 거짓이 되고 출력 되지 않는다

#  __name__ 변수의 특징은 우리가 실행하고자 하는 모듈 내부에서는 거기에 "__main__"이
# 자동 저장되게 설정되어 있다
# import될 때는 __name__에다 <import 당하는 모듈의 이름>이 저장되게 세팅 돼있다 파이썬 내부적으로 
# 예를 들어 04_module_basic03 에서 import calculator as cal 라고 입력하면 
# print("__name__의 값:",__name__)은 __name__의 값: calculator 라고 출력된다


if __name__ == "__main__": # 실행이 된다 --> 즉 True가 나왔다
    print("1~50까지의 누적합:", calc_sum(50))
    print("메롱메롱")





