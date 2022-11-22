# 밑에 while문 보고 함수 만들어보기


# 제품 1개당 필요한 정보
# [제품번호, 제품명, 단가, 수량, 제품총액]
# 이런 비정형적 데이터는 리스트보다 사전이 편리하다 




def show_menu():
    
    print("\n *** 재고 관리 프로그램 ***")
    print(" 1. 제품 정보 등록")
    print(" 2. 모든 제품정보 조회")
    print(" 3. 프로그램 종료")
    print(" ======================")
    
    m = int(input("메뉴: "))
    return m

def reg_product():
    product = {}
    
    print("# 제품 등록을 시작합니다.")
    product['제품번호'] = input("제품번호: ")
    product['제품명'] = input("제품명: ")
    product['단가'] = int(input("단가: "))
    product['수량'] = int(input("수량: "))
    product['제품총액'] = product['단가'] * product['수량']
    
    inventory.append(product)
    print("\n제품 등록이 정상적으로 처리되었습니다.")

def show_all_product():
    all_price = 0 #지역변수 , 제품들의 누적 총합 구하려고 
    print("\n           *** 창고 재고 정보 ***")
    print("=============================================")
    print("제품번호        제품명         수량          단가         제품총액")
    print("=============================================")
    
    for product in inventory:
        all_price += product['제품총액']
        print("%4s      %4s       %4d     %7d %10d" % 
              (product['제품번호'], product['제품명'],
               product['수량'], product['단가'], 
               product['제품총액']))
    print("=============================================")
    print("\t\t\t 창고 재고 제품 총액: %d원" % all_price)

inventory = []


# 이 while문만 보고 함수 만들어 보기
while True:
    
    menu = show_menu()
    
    if menu == 1:
        reg_product()
    elif menu == 2:
        show_all_product()
    elif menu == 3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("메뉴를 잘못 입력했습니다.")
    
    
    
    
    
    
