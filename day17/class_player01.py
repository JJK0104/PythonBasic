'''
메서드의 인수로 또 다시 객체를 받아서 그걸로 self가 계속 달라지는 
'''

'''
1) 클래스 이름 : Warrior
2) 생성자는 user_id만 받기 -> level, hp, atk, exp 만들어지게끔
3) 캐릭터 정보창 보는 기능
4) 레벨업 기능
5) 죽는 기능
6) hp 조정 기능(hp가 0보다 작으면 0으로 처리, 0 이상일 시 그냥 그대로)
7) 다시 살아나는 기능
8) 공격 기능
9) 스킬
'''


class Warrior:
    
    # 생성자부터 만든다
    def __init__(self, user_id):
        
        self.user_id = user_id
        self.level = 1
        self.hp = 50
        self.atk = 3
        self.exp = 0
    
    # 캐릭터 정보창 보는 기능
    def info(self):
        print("\n======캐릭터 정보======")
        print(" 아이디:", self.user_id)
        print(" 레벨:", self.level)
        print(" 공격력:", self.atk)
        print(" 체력:", self.hp)
    
    # 레벨업 기능
    def lev_up(self):
        if self.exp >= 100 + self.level * 20: # 레벨 1 때는 120 이상, 레벨 2 때는 140 이상 ....
            self.level += 1
            self.hp += self.level * 5
            self.atk += 3
            self.exp = 0
            print("%s님의 레벨이 올랐습니다." % self.user_id)
    
        '''
        만약에 한번에 여러번 레벨업 하는 기능을 만들려면
        while 문을 써서 

        근데 지금 여기서 self.exp는 ' 현재 남아 있는 exp' 인듯...
        그래서 따로 self.sum 이라는 거 만들어서 exp 누적합을 구해야 할 거 같기도 하고

        예를 들어 레벨 3 + 50exp 가 있는 상황에서 400exp를 획득하면
        110exp 소모 -> 레벨 4 -> 180exp 소모 -> 레벨 5 + 110exp 남음

        while self.exp >= 100 + self.level * 20:
            self.exp -= 100 + self.level * 20
            self.level += 1
            :
            :
            :

        예를 들어
        l = 1
        exp = 30

        while exp > l*2 + 10 :
            exp -= l*2 + 10
            l = l+1
        '''

    # 죽는 기능
    def die(self):
        if self.hp <= 0:
            print("%s님이 죽었습니다." % self.user_id)
    
    # hp를 조정하는 메서드
    def set_hp(self, hp):
        if hp <= 0: # 체력이 -20인 거 보다는 그냥 0 인게 예쁘니까
            self.hp = 0
        else:
            self.hp = hp
    
    # 다시 살아나는 기능
    def restart(self):
        self.__init__(self.user_id) # self에 메서드 쓰네...
                                    # 죽기전이랑 똑같은데 hp만 풀로 부활하게 하려면?
        print("%s님이 부활했습니다." % self.user_id)
    
    # 공격   *************중요***************
    # p1 = Warrior('전사킹짱짱맨')
    # p2 = Warrior('내꿈은전사왕')
    # p1.attack(p2) 처럼 쓰려고 아래 코드를 만드는 거다
    def attack(self, target): # 인수에 객체 전달

        print("%s님이 %s님에게 일반공격 시전!!" 
              % (self.user_id, target.user_id))
        remain_hp = target.hp - self.atk # 맞은 놈 체력 계산
        target.set_hp(remain_hp)
        
        print("%s님이 %d의 피해를 입었습니다. (남은체력: %d)"
              % (target.user_id, self.atk, target.hp))
        self.exp += 30
        self.lev_up() # 레벨업 할 경우
        target.die() # 상대방이 죽을 경우
   
    # 스킬   *************중요***************
    def power_charge(self, target):
        print("%s님이 %s님에게 파워차지 시전!!"
              % (self.user_id, target.user_id))
        # print("{}님이 {}님에게 일반공격 시전!!" 
        #     .format(self.user_id, target.user_id))
        
        damage = self.atk * 2
        remain_hp = target.hp - damage
        target.set_hp(remain_hp)
        
        print("%s님이 %d의 피해를 입었습니다. (남은체력: %d)"
              % (target.user_id, damage, target.hp))
        self.exp += 50
        self.lev_up() # 레벨업 할 경우
        target.die() # 상대방이 죽을 경우
        
if __name__ == '__main__':
    
    p1 = Warrior('전사킹짱짱맨')
    p2 = Warrior('내꿈은전사왕')
    
    p1.info() 
    # p1의 타입은 Warrior다. Warrior 타입은 인덱싱, 슬레이싱 못 한다
    # Warrior타입이 할 수 있는 건 . 을 통해 hp, exp에 접근하고 attack, lev_up등을 사용
    # p1이 info를 부르면 info의 self에 p1이 들어간다
    p2.info()    
    
    p1.attack(p2)
    
    p2.power_charge(p1)
    
    p1.power_charge(p2)
    # power_charge(self,target)의 self에는 p1이 들었고 target에는 p2가 들었다. 인수에도 객체 전달할 수 있다.
    # damage = p1.atk * 2
    # target.hp 는 p2.hp
    # p2.set_hp(remain_hp)가 콜됐음. 함수 실행중에 중간에 다른 함수가 다시 콜 되면
    # 그 중간 함수가 다 끝날때 까지 코드가 못 내려감. set_hp로 갑시다
    # set_hp의 self는 p2다, hp는 remain_hp
    # 이제 set_hp가 끝나면 다시 power_charge로 돌아와서 밑에 코드를 실행한다
    # self.exp 의 self는 p1

    # .은 참조 연산자(reference operator)
    # p1.은 "p1이 주목하는 주소로 향해라" 라는 뜻이다. 여기서 p1.power_charge(p2) 라 하면 p1의 주소로 가서 거기있는 power_charge를 불러서 p2를 전달해
    # p2.은 p2가 지목하는 주소로 향해라 

    # 광역 공격은 targets = [] 에 여러 target을 넣어주면 된다. 그리고 반복문 돌려주면 됨
    p1.power_charge(p2)    
    p1.power_charge(p2)
    p1.power_charge(p2)
    p1.power_charge(p2)
    
    p1.info()
    
    p2.restart()
    p2.info()
    
    
    
    
    
    
    



