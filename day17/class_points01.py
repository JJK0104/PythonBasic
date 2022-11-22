# 학생들 성적 처리하는 class 만들기 

class Student:
    
    # Student 객체를 만들면 아래의 8가지 변수가 메모리에 들어온다
    def __init__(self):
        self.id = None # input으로 입력받아 넣을 거기 때문에 일단은 None으로 
        # 정해지지 않은 data를 만들어 놓을 때는 다른 언어는 그냥 ; 찍으면 되는데 파이썬은 그렇게 못함
        # 무조건 뭔가가 들어가 있어야됨
        # 어떤 걸 None이라고 쓰냐면 객체 data 주소가 들어갈 변수는 None이라고 쓴다. 아직 정해지지 않은
        # 예를 들면 str, 리스트, 튜플, 딕셔너리, 클래스
        self.name = None
        self.kor = 0 # 정수가 들어갈 data가 정해지지 않았으면 0
        self.eng = 0
        self.math = 0
        self.tot = 0
        self.avg = 0.0 # 실수가 들어갈 data가 정해지지 않았으면 0.0
        self.grade = None
    
    # 성적 정보 입력 기능
    # 객체를 통해 input_stu_info()를 호출하면 5가지 data를 입력받을 수 있다
    def input_stu_info(self):
        
        self.id = input("학번: ")
        self.name = input("이름: ")
        self.kor = int(input("국어: "))
        self.eng = int(input("영어: "))
        self.math = int(input("수학: "))
    
    # 총점, 평균 구하는 기능
    # 객체를 통해 calc_tot_avg_grade()를 호출하면 self.tot, self.avg, self.grade 3가지 정보를 저장할 수 있다
    def calc_tot_avg_grade(self):
        
        self.tot = self.kor + self.eng + self.math
        self.avg = self.tot / 3
        
        if self.avg >= 90:
            self.grade = 'A'
        elif self.avg >= 80:    
            self.grade = 'B'
        elif self.avg >= 70:    
            self.grade = 'C'
        elif self.avg >= 60:    
            self.grade = 'D'
        else:
            self.grade = 'F'

    # 학생 성적 정보 출력하는 기능
    def output_stu_info(self):
        
        print("%4s   %8s     %3d   %3d   %3d   %3d   %3.2f %3s"
              % (self.id, self.name, self.kor,
                 self.eng, self.math, self.tot,
                 self.avg, self.grade))
    
# 메서드가 아닌 함수 
def show_points_ui():
    
    print("\n            *** 성적표 ***")
    print("="*90)  
    print("학번         이름      국어      영어      수학     총점     평균     학점")
    print("="*90)  
    
    
if __name__ == '__main__':
    '''
    만약 리스트 형태로 안 하고 그냥 아래처러 만들면
    for x in range(3):
        stu = student()
        stu.input_stu_info()
        stu.calc_tot_avg_grade

    첫 실행 때 0x10(가상의 주소)에 8개의 정보가 입력된다 그리고 이 0x10주소가 stu에 저장된다
    두번째 실행 때 student객체가 또 메모리에 생성된다 다른 주소(0x20)에 그리고 0x20을 stu에 저장한다
    그럼 stu가 가리키는 곳이 0x20으로 바뀌면서 0x10을 기억해주는 애가 하나도 없어짐
    3번째가 만들어지면 2번째, 1번째 미아됨

    그래서 주소를 여러개 저장할 수 있는 리스트 만든다
    
    '''

    students = []
    
    for x in range(3):
        s = Student()
        print(s) # <__main__.Student object at 0x00~~~>
        s.input_stu_info()
        print("\n")
        s.calc_tot_avg_grade()
        students.append(s)


    show_points_ui()
    for s in students:
        s.output_stu_info()





