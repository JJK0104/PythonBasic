# class_player01 모듈에서 Warrior라는 클래스 정보 얻어 올건데 소속을 안 밝히고 쓰겠다
# 예를 들면 p1 = Warrior("킹왕짱짱맨")
from class_player01 import Warrior 
# 만약 그냥 import class_player01 이면 
# p1 = class_player01.Warrior("킹왕짱짱맨")라고 써야됨



# 2 번째 직업
class Priest:
    
    def __init__(self, user_id):
        
        self.user_id = user_id
        self.level = 1
        self.hp = 45
        self.atk = 2
        self.exp = 0
    
    def info(self):
        print("\n======캐릭터 정보======")
        print(" 아이디:", self.user_id)
        print(" 레벨:", self.level)
        print(" 공격력:", self.atk)
        print(" 체력:", self.hp)

    def lev_up(self):
        if self.exp >= 100 + self.level * 20:
            self.level += 1
            self.hp += self.level * 5
            self.atk += 3
            self.exp = 0
            print("%s님의 레벨이 올랐습니다." % self.user_id)
    
    def die(self):
        if self.hp <= 0:
            print("%s님이 죽었습니다." % self.user_id)
    
    def set_hp(self, hp):
        if hp <= 0:
            self.hp = 0
        else:
            self.hp = hp
    
    def restart(self):
        self.__init__(self.user_id)
        print("%s님이 부활했습니다." % self.user_id)
    
    def attack(self, target):
        
        print("%s님이 %s님에게 일반공격 시전!!" 
              % (self.user_id, target.user_id))
        remain_hp = target.hp - self.atk
        target.set_hp(remain_hp)
        
        print("%s님이 %d의 피해를 입었습니다. (남은체력: %d)"
              % (target.user_id, self.atk, target.hp))
        self.exp += 30
        self.lev_up()
        target.die()
    
    # 힐 스킬
    def heal(self, target):
        
        print("%s님이 %s님에게 치유 시전!!" 
              % (self.user_id, target.user_id))
        
        # 힐량
        heal_amt = self.level * 7
        remain_hp = target.hp + heal_amt
        target.set_hp(remain_hp)
        
        print("%s님이 %d의 체력을 회복했습니다. (남은체력: %d)"
              % (target.user_id, heal_amt, target.hp))
        self.exp += 40
        self.lev_up()

if __name__ == '__main__':
    
    # p1 = class_player01.Warrior('킹갓빛황전사') 는 안된다. 왜냐면 from class_player01 import Warrior 했으니까
    p1 = Warrior('킹갓빛황전사')
    p2 = Priest('힐받으면내꼬')
    
    p1.power_charge(p2)
    p1.power_charge(p2)
    p1.power_charge(p2)
    p1.power_charge(p2)
    p1.power_charge(p2)
    
    p2.heal(p2)
    p2.heal(p2)
    p2.heal(p2)
    p2.heal(p2)
    p2.heal(p2)





