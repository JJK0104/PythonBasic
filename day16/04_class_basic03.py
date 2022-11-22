'''
* 클래스

- 클래스는 객체(물건)를 만들기 위한 틀(도면)입니다.
- 클래스는 객체의 속성(변수)과 기능(메서드)의 집합입니다.
- 클래스 내부에 정의된 함수를 메서드라고 부릅니다.
'''
class Calculator: # 도면이름, 관례적으로 앞글자는 대문자
    
    # 클래스 내부에 들여쓰기와 함께 정의된 함수를 '메서드'라고 부른다
    # 얘네들은 함수처럼 그냥 부른다고 작동하지 않는다
    # 반드시 어떤 객체를 통해 불렀는지 알려줘야 되기 때문에 self가 들어간다
    # 이 self가 의미하는 건 누구의 setting인가

    # 그래서 메서드 특징은 첫번째 인자값으로 반드시 self가 온다
    # 함수는 self를 쓸 수 없지만 메서드는 무조건 self를 써야한다
    # 나머지는 기존의 함수 인자를 입력하듯이 입력
    def setting(self, color, n1, n2): # self는 자동으로 들어가고 변수를 color, n1, n2 총 3개 주세요
        
        # color, n1, n2는 인수, 지역변수 개념
        # self가 붙어있는 변수를 멤버변수라고 부릅니다.
        # 멤버 변수는 '클래스에 소속되어있는 변수'이며 클래스의 속성(Attribute)을 의미합니다
    
        
        # 인수 이름이랑 멤버변수 이름 똑같이 안 만들어도 됨(self.color = color로 안 만들어도 됨)
        # self.c = color 이렇게 만들어도 됨
        self.color = color # 인수 color를 Calculator의 속성인 color(즉, self.color)에 저장하세요
                           # 만약 self.c = color 라면 인수 color를 Calculator의 속성인 c(즉, self.c)에 저장하세요
        self.nf = n1
        self.n2 = n2
    
    def add(self): # self는 자동으로 들어가고 data 0 개 주면된다
        result = self.nf + self.n2 # result는 지역변수
                                   # self.nf, self.n2 는 다른 함수(메서드) setting에 있는건데 쓰네... 지역변수 개념이 아닌가... ??
                                   
                                   # self가 붙어있는 변수를 멤버변수라고 부릅니다.
                                   # 멤버 변수는 '클래스에 소속되어있는 변수'이며 클래스의 속성(Attribute)을 의미합니다

                                   # self.이 붙어있는 변수, 즉 멤버 변수를 class 내 전역벼수라고 생각하는 게 나을라나..?

                                   # self.nf, self.n2는 setting 메서드가 작동된 뒤에 생긴다
                                   # 그래서 setting 메서드 안 쓰고 add 메서드를 먼저쓰면 오류발생함
                                   # AttributeError : 'Calculator' object has no attribute 'nf' 라고 문구뜬다...
                                   # 'nf'만 없다고 뜨네... self.nf 이후로 진행이 안 돼서 그런듯
        return result

# 도면을 만들었으면 이제 도면으로 물건 만들기 = 객체 생성
'''
- 클래스가 정의되었다면 해당 클래스를 통해 빠르게 객체를 생성할 수 있습니다.

- 객체 생성 문법
ex) 변수 = 클래스명()
ex) list1 = list()
'''
red_calc = Calculator() # 빨강 계산기 객체 생성
blue_calc = Calculator() # 파랑 계산기 객체 생성
# list1 = list()


# 클래스의 메서드 호출 => 객체변수명.메서드명() ex) list.append(2)
red_calc.setting('빨강색', 15, 5) 
# .은 참조 연산자(reference operator)
# red_calc.은 red_calc가 지목하는 주소로 향해라 그리고 거기있는 setting을 불러서 3개 data를 전달해주세요
# 그리고 setting의 self에는 red_calc(주소)가 들어간다, color에는 '빨강색', n1 에는 15, n2 에는 5
# 이제 메서드가 호출 됐으니 내부가 실행됨 
# 0x10(red_cal 주소라 가정) color 영역에 color의 값을 저장하세요
# 0x10(red_cal 주소라 가정) color 없으면 생성하고 만약에 이미 있으면 변경
# 0x10(red_cal 주소라 가정) nf, n2 영역도 마찬가지
blue_calc.setting('파랑색', 20, 15)


# 클래스의 멤버변수 호출 => 객체변수명.멤버변수명
print("파랑계산기 색깔(self.color):", blue_calc.color) # 여기서 .color라고 하는 건 self.color = color로 해서다
                                                      # 만약 self.c = color로 했으면 blue_calc.c 로 써야됨
print("빨강계산기 색깔(self.color):", red_calc.color)

red_calc.setting('노랑색',15,5)
print("빨강계산기 색깔(self.color):", red_calc.color) # 빨강계산기 색깔(self.color): 노랑색

print("파랑계산기 덧셈결과:", blue_calc.add())
print("빨강계산기 덧셈결과:", red_calc.add())


print(type(red_calc))
print(type(blue_calc))

print(id(red_calc)) 
print(id(blue_calc)) # red_calc, blue_calc 주소는 계속 바뀌는데 
print(id(red_calc)-id(blue_calc)) # -200992로 일정하네

red_calc.setting("검정색",12,12) # red_calc 한번 더 생성해도
print(id(red_calc)-id(blue_calc)) # -200992로 일정하네 
print('\n\n\n\n'+'-'*40)

black_calc = Calculator()
# a = black_calc.add() # black_calc.setting('검정색',15,20) 을 먼저 해줘야 
                       # self.nf, self.n2 가 생김

