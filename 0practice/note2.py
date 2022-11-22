'''
메서드의 인수로 또 다시 객체를 받아서 그걸로 self가 계속 달라지는 
'''

'''
1) 클래스 이름 : Warrior
2) 생성자는 user_id만 받기
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
        self.__init__(self.user_id)
        print("%s님이 부활했습니다." % self.user_id)
    
    # 공격
    def attack(self, target):
        
        print("%s님이 %s님에게 일반공격 시전!!" 
              % (self.user_id, target.user_id))
        remain_hp = target.hp - self.atk # 맞은 놈 체력 계산
        target.set_hp(remain_hp)
        
        print("%s님이 %d의 피해를 입었습니다. (남은체력: %d)"
              % (target.user_id, self.atk, target.hp))
        self.exp += 30
        self.lev_up() # 레벨업 할 경우
        target.die() # 상대방이 죽을 경우
    # 스킬 
    def power_charge(self, target):
        print("%s님이 %s님에게 파워차지 시전!!"
              % (self.user_id, target.user_id))
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

    
    '''
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


    # 광역 공격은 targets = [] 에 여러 target을 넣어주면 된다. 그리고 반복문 돌려주면 됨
    p1.power_charge(p2)    
    p1.power_charge(p2)
    p1.power_charge(p2)
    p1.power_charge(p2)
    
    p1.info()
    
    p2.restart()
    p2.info()
    
    
    
    '''
    
    
    



