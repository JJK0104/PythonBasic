from class_points01 import Student, show_points_ui
# class_points01 모듈에서 Student, show_points_ui 라는 클래스, 함수 정보를 얻어 올건데 소속을 안 밝히고 쓰겠다
# 예를 들면 stu = Student()
# 만약 그냥 import class_points01 이면 
# stu = class_points01.Student()라고 써야됨


def menu_info():
    
    print("\n *** 성적관리 프로그램")
    print(" 1. 성적정보 입력")
    print(" 2. 전체성적 조회")
    print(" 3. 개인성적 조회")
    print(" 4. 성적정보 수정")
    print(" 5. 성적정보 삭제")
    print(" 6. 프로그램 종료")
    print()
    
def f_input():
    '''
    1. 학생의 객체를 1개 생성합니다.
    2. 학생의 객체에 속성값을 설정하는 메서드들을 호출!
    3. 정보저장이 완료된 객체를 리스트에 추가!
    4. 저장완료 메세지를 출력하세요.
    '''
    stu = Student()
    stu.input_stu_info()
    stu.calc_tot_avg_grade()
    students.append(stu)
        
    print("%s님의 성적정보 입력이 정상 처리되었습니다." % stu.name)

def f_output():
    '''
    1. 리스트 안에 들어있는 학생객체들의 정보를 
       반복문을 통해 전체 출력하세요.
    2. 우리반의 전체평균을 가장 아랫부분에 출력하세요.
    '''
    total_avg = 0.0
    show_points_ui()
    for stu in students:
        total_avg += stu.avg
        stu.output_stu_info()
    print("================================================")
    print("\t\t\t 우리 반 전체평균: %.2f점" 
          % (total_avg / len(students)))

def f_search():
    print("성적을 조회할 학생의 학번을 입력하세요.")
    stu_num = input("=> ")    
    '''
    1. 해당 학번과 일치하는 학생객체를 리스트에서 찾아내서
     그 학생의 정보만 출력하세요.
    2. 찾는 학번이 없을시 검색하지 못했다는 메시지를 출력
     하세요.
    '''
    for stu in students:
        if stu_num == stu.id: # 이거 stu를 studen으로 바꿔서 실행해보기, 위에 for문의 stu도 똑같이 바꿔서
            show_points_ui()
            stu.output_stu_info() # 여기 stu도 studen으로 바꿔서
            break
    else:
        print("조회하신 학번정보 '%s'는 입력되지 않은 학번입니다."
              % stu_num)

def f_update():
    print("성적을 수정할 학생의 학번을 입력하세요.")
    stu_num = input("=> ")    
    '''
    1. 해당 학번과 일치하는 학생객체를 리스트에서 찾아내서
     그 학생의 국어,영어,수학 점수를 수정하세요.
    2. 찾는 학번이 없을시 검색하지 못했다는 메시지를 출력
     하세요.
    '''
    for stu in students:
        if stu_num == stu.id:
            print("\n%s님의 성적을 수정합니다." % stu.name)
            stu.kor = int(input("국어: "))
            stu.eng = int(input("영어: "))
            stu.math = int(input("수학: "))
            stu.calc_tot_avg_grade()
            print("성적 수정이 정상 처리되었습니다.")
            break
    else:
        print("조회하신 학번정보 '%s'는 입력되지 않은 학번입니다."
              % stu_num)

def f_delete():
    print("성적을 삭제할 학생의 학번을 입력하세요.")
    stu_num = input("=> ")    
    '''
    1. 해당 학번과 일치하는 학생객체를 리스트에서 찾아내서
     그 학생의 모든 정보를 삭제하세요.
    2. 찾는 학번이 없을시 검색하지 못했다는 메시지를 출력
     하세요.
    '''   
    for stu in students:
        if stu_num == stu.id:
            print("\n%s님의 성적을 삭제합니다." % stu.name)
#             students.remove(stu) 주소를 직접 넣어 삭제
            del(students[students.index(stu)]) # 번호로 삭제
            print("성적 삭제가 정상 처리되었습니다.")
            break
    else:
        print("조회하신 학번정보 '%s'는 입력되지 않은 학번입니다."
              % stu_num)  
    
students = []

while True:
    
    menu_info()
    try:
        menu = int(input("메뉴 선택: "))
    except:
        print("메뉴는 숫자로만 입력하세요!")
        continue
    
    if menu == 1:
        f_input()
    elif menu == 2:
        f_output()
    elif menu == 3:
        f_search()
    elif menu == 4:
        f_update()
    elif menu == 5:
        f_delete()
    elif menu == 6:
        print("프로그램을 종료합니다.")
        break
    else:
        print("메뉴를 잘못 입력했습니다.")

    
    
    