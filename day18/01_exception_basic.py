'''
크게 시스템상 오류(예외)에는 2가지가 있다
Error 와 Exception
Error는 심각한 거. 프로그램 외적인 원인으로 발생한다. 운영체제에 문제가 생겼다던가.
Exception은 순한 거. 문법적인 처리를 잘못 했거나 사용자가 프로그램을 잘못 사용할 경우 발생
'''

'''
* 예외 처리

- 프로그램은 실행 중에 사용자와 끊임없는 상호작용을 합니다.

- 그러나 프로그램의 사용자는 예측불가의 행동을 할 수 있으며
  잘못된 사용으로 인해 에러를 발생시킬 수 있습니다.

- 프로그램에서 예외가 발생하면 프로그램이 비정상 종료되기 때문에
  예외처리 문법을 통해 프로그램이 정상 작동할 수 있도록 코드를 
  구성해야 합니다.
  
- 예외처리 키워드는 try ~ except를 사용합니다.

- try블록 내부에는 예외 발생 가능성이 있는 코드를 작성합니다.
  ex) int(input()) <- 숫자를 안 적으면 에러 난다

- except에는 try에서 예외가 발생할 시 처리할 코드를 작성합니다.
  ex) print('숫자로 입력해주세요')

- try 내부에서 예외가 발생한다면 즉시 try의 실행을 중단하고
  except의 코드를 실행합니다.
'''



n1 = 10
n2 = 0
try : 
    result = n1/ n2
    print("%d / %d = %d" %(n1, n2, result))
except :
    print("0으로 나눌 수 없습니다.")
print("프로그램 정상 종료\n\n")
'''
if - else도 예외처리중 하나 
그런데 if - else는 에러 사항을 회피하는 거다. 0이 들어오는 상황을 분기로 나눠서 아예 실행이 안 되게 만들어서 흘려보낸다
 
try - except는 에러 상황을 정면으로 받아들임

'''


'''
* 다중 예외처리
- 한 개의 try블록에서 발생하는 예외의 원인에 따라 다르게 예외처리를
  하는 방법.

- 자주 발생하는 예외
1. NameError: 정의되지 않은 변수, 함수, 클래스를 사용할 때 발생
2. ValueError: 주로 형 변환 시 내부 값의 형식이 잘못되었을 때 발생
  ex) int("3.14")
3. ZeroDivisionError: 숫자를 0으로 나눌 경우 발생.
4. IndexError: 문자열이나 리스트 등 시퀀스 데이터의 
  존재하지 않는 인덱스를 참조했을 경우 발생.
  ex) s = 'hello'
      print(s[6])
5. TypeError: 연산 수행시 데이터의 타입이 일치하지 않을 경우 발생.
  ex) print(10 ** "hello")
'''
while True:
    try:
        n1 = int(input("정수1: ")) # 여기서 40'점' 이라고 입력하면 바로 에러발생해서 except ValueError로 간다
        n2 = int(input("정수2: "))
        result = n1 / n2  
        print("%d / %d = %d" % (n1, n2, result))
        break
    except ValueError:
        print("숫자로만 입력하세요~")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except: # 이렇게 멀티 except 사용시 만능 except는 마지막에
        print("알 수 없는 오류 발생! 점검 후 조치하겠습니다!")
    

print("프로그램 정상 종료!!")








