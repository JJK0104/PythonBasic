'''
* 생성자 (Constructor)

- 생성자는 객체가 생성될 때 
  클래스의 멤버변수(self변수, self.balance 같은 것들)를 초기화하거나 
  객체 생성과 동시에 해야할 작업을 기술하는 데 사용합니다.

- 생성자 이름은 __init__ 으로 정해져 있다
  파이썬에서는 클래스 내부의 메서드 이름을 __init__로 작성하면
  이 메서드를 자동으로 생성자로 취급하게 됩니다.

- 메서드는 원래 호출해줘야만 작동하는데 
  생성자는 객체 생성 명령에 의해 자동으로 호출됩니다.
'''

class Test:

    # 생성자 정의
    def __init__(self):
        print("생성자가 호출됨!!")

# if __name__ == '__main__': 쓰는 이유 day 15 calculator 보기
if __name__ == '__main__':
    
    # 객체 생성 명령을 내리면 시스템상 자동적으로 __init__이 불려짐
    woori = Test() # 생성자가 호출됨!!  이 출력됨
    # 원래 메서드 작동시킬려면 아래처러 해야됨
    # woori.__init__() 
    

print()
print()

class Account:
    
    # 생성자 정의
    # 생성자를 통해 초기값을 상수로 설정하는 게 아니라 전달 받아서 설정할 수도 있다
    def __init__(self, bank, owner, password):
        self.balance = 0
        self.bank = bank
        self.owner = owner
        self.pw = password #인수 이름이랑 멤버변수 이름 똑같이 안 만들어도 됨
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, money):
        self.balance += money
        
        
    def withdraw(self, money):        
        self.balance -= money


if __name__ == '__main__':
    
    woori = Account('우리은행', '홍길동', 1234) # 생성자를 통해 초기값을 상수로 설정하는 게 아니라 전달 받아서 설정할 수도 있다
#     woori.__init__()이 자동으로 실행되고
#     self.balance = 0, woori.bank = '우리은행', woori.owner = '홍길동', woori.pw = 1234 됨

    woori.deposit(15000)
    print("%s 잔액: %d원" % (woori.bank, woori.get_balance()))
    print("[예금주: %s님, 비밀번호: %d]"
          % (woori.owner, woori.pw))




