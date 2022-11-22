# 프로그래밍 할 때 관리의 편의성을 위해 함수화 할 수 있는 건 다 함수화 해라
# day 11의 01_food_menu도 할 수 있으면 해보기 
# 함수는 가능하면 위에 모아놔라

# 맨 아래 while문 코드만 보고 한번 함수 만들어봐라

'''
while True:
    
    menu = show_menu() 
    
    if menu == 1:
        odd_gugudan()
    elif menu == 2:
        even_gugudan()
    elif menu == 3:
        dan = int(input("단수: "))
        select_gugudan(dan)
    elif menu == 4:
        print("프로그램을 종료합니다.")
        break
    else:
        print("메뉴를 잘못 입력했습니다.")

1번 선택시 홀수구구단 다 보여주기
2번 선택시 짝수구구단 다 보여주기
3번 선택시 해당 구구단 보여주기
4번 선택시 종료

'''


def show_menu():
    print("\n *** 구구단을 외자~~ ***")
    print(" 1. 홀수 구구단 보기")
    print(" 2. 짝수 구구단 보기")
    print(" 3. 특정 구구단 보기")
    print(" 4. 프로그램 종료")
    print(" ********************")
    menu = int(input("메뉴: "))
    return menu

def print_hang(dan):
    print("구구단 %d단" % dan)
    print("-" * 40)
    for hang in range(1, 10):
        print("%d x %d = %d" 
                % (dan, hang, dan * hang))
    print("-" * 40)

def odd_gugudan():
    for dan in range(2, 10):
        if dan % 2 != 0:
            print_hang(dan)

def even_gugudan():
    for dan in range(2, 10):
        if dan % 2 == 0:
            print_hang(dan)

def select_gugudan(dan):
    print("선택하신 구구단을 출력합니다!")
    print_hang(dan)


# 아래코드만 보고 함수들 만들어보기
while True:
    
    menu = show_menu() 
    
    if menu == 1:
        odd_gugudan()
    elif menu == 2:
        even_gugudan()
    elif menu == 3:
        dan = int(input("단수: "))
        select_gugudan(dan)
    elif menu == 4:
        print("프로그램을 종료합니다.")
        break
    else:
        print("메뉴를 잘못 입력했습니다.")
    
    
    
    
    
    