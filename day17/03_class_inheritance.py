# Warrior, Priest, 마법사 등 여러 직업을 만드는데
# 매번 만들면 귀찮다
# 그래서 복사본을 떠놓고 붙여넣기로 자동으로 해줄 순 없을까?
# 그래서 부모님이 자식한테 유산 물려주듯이 해주는 거

# 상속(inheritance)
# - 새로운 클래스를 설계할 때 
#   공통 기능들을 물려줘서 클래스 확장의 시간과 비용을 절감할 수 있게 함




# 부모 클래스(parent class, super class)
# 변수와 메서드를 물려주는 클래스
# __init__ 은 기본 hp, atk 같은 게 다를 수도 있으니까 제외하고 완전 공통 기능만 
class Player:
    def info(self):
        print("\n======캐릭터 정보======")
        print(" 아이디:", self.user_id)
        print(" 레벨:", self.level)
        print(" 공격력:", self.atk)
        print(" 생명력:", self.hp)

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
        
'''
* 자식 클래스 (child class, sub class)
- 변수와 메서드를 물려받는 클래스를 자식클래스라고 합니다.
- 파이썬의 상속표현은 클래스 이름 뒤에 데이터를 물려받을
  부모클래스의 이름을 적어줍니다.
'''       
class Warrior(Player):
    
    def __init__(self, user_id):
        
        self.user_id = user_id
        self.level = 1
        self.hp = 50
        self.atk = 3
        self.exp = 0
    
    def power_charge(self, target):
        print("%s님이 %s님에게 파워차지 시전!!"
              % (self.user_id, target.user_id))
        damage = self.atk * 2
        remain_hp = target.hp - damage
        target.set_hp(remain_hp)
        
        print("%s님이 %d의 피해를 입었습니다. (남은체력: %d)"
              % (target.user_id, damage, target.hp))
        self.exp += 50
        self.lev_up()
        target.die()
   
class Priest(Player):
    
    def __init__(self, user_id):
        
        self.user_id = user_id
        self.level = 1
        self.hp = 45
        self.atk = 2
        self.exp = 0  
   
    def heal(self, target):
        
        print("%s님이 %s님에게 치유 시전!!" 
              % (self.user_id, target.user_id))
        
        heal_amt = self.level * 7
        remain_hp = target.hp + heal_amt
        target.set_hp(remain_hp)
        
        print("%s님이 %d의 체력을 회복했습니다. (남은체력: %d)"
              % (target.user_id, heal_amt, target.hp))
        self.exp += 40
        self.lev_up()
   
   

p1 = Warrior('파워차지맨')
p2 = Priest('대사제김치유')  
        
p1.info()   
p2.info()    
        
# 그리고 또 예를 들어 Warrior가 전직을 해서 SuperWarrior, UltraWarrior가 된다고 하면
# class SuperWarrior(Warrior)로 만들면 Warrior거도 다 물려받고 Player도 물려 받는다 
        
        
        