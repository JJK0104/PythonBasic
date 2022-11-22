'''
* 연습 - 계좌를 관리하기 위한 클래스를 구성해보세요.
1. 클래스의 이름은 Account입니다.
2. 클래스의 첫번째 메서드는 계좌 초기 잔액(self.balance)
   을 셋팅하는 메서드입니다.
- 메서드 이름은 set_balance(self, balance)
3. 2번째 메서드는 계좌 잔액을 조회할 수 있는 메서드입니다.
- 이름은 get_balance로 해주시고 잔액(self.balance)를
   리턴해주세요.
4. 3번째 메서드는 계좌에 입금하는 기능입니다.
- 이름은 deposit으로 하시고 입금액을 전달받아서 
   self.balance에 더해주세요.
5. 4번째 메서드는 계좌에서 돈을 출금하는 기능입니다.
- 이름은 withdraw, 출금액을 전달받아서 
  self.balance에서 빼주세요.

'''
class Account:
    
    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance
    
    def deposit(self, money):
        self.balance += money
        #self.balance = self.balance + money
        
    def withdraw(self, money):        
        self.balance -= money

# test 코드       
if __name__ == '__main__':
    
    shinhan = Account()
    kookmin = Account()
    
    # set_balance 메서드가 호출 되지 않으면 self.balance가 메모리 영역에 만들어지지 않는다
    # 만약 self.balance가 만들어지지 않은 채로 get_balance, deposit, withdraw 실행시키면 작동 안된다
    shinhan.set_balance(20000)
    kookmin.set_balance(12000)
    
    shinhan.deposit(10000)
    shinhan.withdraw(24000)
    
    kookmin.deposit(7000)
    kookmin.withdraw(5000)
    
    print("신한은행 잔액:", shinhan.balance)
    print("국민은행 잔액:", kookmin.get_balance())
    
    print('\n\n\n\n\n\n'+'-'*40)
    woori = Account()
    
    woori.deposit(5000)
    #'Account' object has no attribute 'balance' 오류뜬다... 여기서 'balance'는 self.balance의 'balance'다
    # self.balance는 set_balance 내부에서 만들어진다
    # set_balance를 불러줘야만 Account 내부에 self.balance가 생성된다
    # self.balance가 있어야 get_balance, deposit,withdraw를 할 수 있다
    # 없는 걸 return하고 더할 수는 없으니
 
 
 
 
        