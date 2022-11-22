

'''
* raise

- 프로그램 내부에서 raise를 만나는 순간 강제로 예외가 발생하게 됩니다.
- 보통 함수를 호출할 때 예외처리 구문 try~except를 강요하고 싶을 때
  사용하는 키워드입니다.
'''
def withdraw(money):
    # 잔액보다 많이 출금 못 하게 하기 위해 만든 코드
    # if money > balance:
    #    print("잔액이 부족합니다.")
    #    return
    # 하지만 위 코드 실행되면 None이 return된다
    
    
    if money > balance:
        raise ValueError
    return balance - money

balance = 5000

try:
    result = withdraw(3000)
    print("출금 후 잔액: %d원" % result)
except:
    print("잔액이 부족합니다.")






