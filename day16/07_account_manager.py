# class_constructor 모듈에서 Account라는 클래스 정보 얻어 올건데 소속을 안 밝히고 쓰겠다
# 예를 들면 shinhan = Account()
from class_constructor import Account # 04_module_basic03 처럼 실행시키면 얘 때문에
                                      # class_constructor 의 print()print() 가 출력됨
# 만약 그냥 import class_constructor 이면 
# shinhan = class_constructor.Account()라고 써야됨
'''
우리가 import하는 거... 이거 쓰기 귀찮아서 import 하는 거임... 미리 만든 거 있으니까
import 안 하고 아래 코드 쓰면 정상 작동됨
import 해도 이렇게 쓰면 정상 작동 됨
만약 여기서 Account 클래스를 바꾸면 어떻게 될까? 안 해봄
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
'''
def menu_info():
    
    print("\n *** 계좌 관리 프로그램 *** ")
    print("1. 계좌 정보 조회")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 잔액 조회")
    print("5. 프로그램 종료")

# 계좌 정보를 등록하는 함수
def reg_account():
    
    bank_name = input("은행명: ")
    owner_name = input("예금주명: ")
    password = int(input("비밀번호: "))
    
    # 계좌 객체 생성
    acc = Account(bank_name, owner_name, password) # acc는 지역변수
                                                   # 여기서 지역변수 헷갈리면 day16-04_class_basic03 보기
    print("%s님의 계좌가 등록되었습니다." % acc.owner)
    return acc # acc는 지역변수니까 따로 빼놔서 저장시킴. 
    # 밑에 while True 위에 my_acc = reg_account() 로

# 1번 메뉴에 해당하는 기능.
def account_info():
   
    print("*** 나의 계좌 정보 ***")   # 밑에 while True 위에 my_acc = reg_account() 로 만듦
    print("은행명: %s" % my_acc.bank) # my_acc라는 전역변수를 통해 은행명 bank라는 self 변수에 접근하고
    print("예금주명: %s" % my_acc.owner)
    print("잔액정보: %d원" % my_acc.get_balance()) # reg_account()에서 만든 acc 정보,주소값을 my_acc에 대입해놨으니
    print("********************")
   

# 2번 메뉴에 해당하는 기능.
def deposit_acc():
    password = int(input("비밀번호를 입력: "))
    
    # 비번이 일치하면 입금액을 입력받아 
    # 입금메서드 호출    
    if password == my_acc.pw:
        money = int(input("입금액: "))
        my_acc.deposit(money)
        print("입금이 완료되었습니다.")
    else:
        print("비밀번호가 틀렸습니다.")
    

# 3번 메뉴에 해당하는 기능.
def withdraw_acc():
    password = int(input("비밀번호를 입력: "))
    
    # 비번이 일치하면 출금액을 입력받아
    # 출금액이 현재잔액보다 크다면 잔액부족
    # 메세지와 함께 출금을 해주면 안됨!    
    if password == my_acc.pw:
        money = int(input("출금액: "))
        if money < my_acc.get_balance():
            my_acc.withdraw(money)
            print("출금이 완료되었습니다.")
        else:
            print("잔액이 %d원 부족합니다."
                  % (money - my_acc.balance))
    else:
        print("비밀번호가 틀렸습니다.")
    

# 4번 메뉴에 해당하는 기능
def check_acc():
    print("잔액정보: %d원" % my_acc.get_balance())
    



# 계좌 정보를 저장할 전역변수 my_acc
my_acc = reg_account()



while True:
    
    menu_info()
    menu = int(input("메뉴: "))
    
    if menu == 1:
        account_info()
    elif menu == 2:
        deposit_acc()
    elif menu == 3:
        withdraw_acc()
    elif menu == 4:
        check_acc()
    elif menu == 5:
        print("프로그램을 종료합니다.")
        break
    else:
        print("메뉴를 잘못 입력했습니다.")
    print("\n\n")




