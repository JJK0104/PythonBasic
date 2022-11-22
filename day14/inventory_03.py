# list 관련 함수 내용 -> day9

def show_menu():
    
    print("\n *** 재고 관리 프로그램 ***")
    print(" 1. 제품 정보 등록")
    print(" 2. 모든 제품정보 조회")
    print(" 3. 개별 제품정보 조회")
    print(" 4. 제품정보 수정")
    print(" 5. 제품정보 삭제")
    print(" 6. 프로그램 종료")
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
    all_price = 0
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

def input_info(info): # 이 코드는 search_product(), modify_product(), delete_product() 에 사용된다
    print("\n *** 제품 정보를 %s합니다." % info)
    print("# %s하실 제품의 코드번호를 입력하세요." % info)
    code = input("제품번호: ")
    return code

def print_product_info(product): # 함수 search_product()에 쓰일 코드... 길어서 
    print("\n           *** [%s] %s 재고 정보 ***"
                  % (product['제품번호'], product['제품명']))
    print("=============================================")
    print("제품번호        제품명         수량          단가             제품총액")
    print("=============================================")
    print("%4s      %4s       %4d     %7d %10d" % 
              (product['제품번호'], product['제품명'],
               product['수량'], product['단가'], 
               product['제품총액']))
    print("=============================================")

def search_product():
    
    code = input_info('조회')
    
    for product in inventory:
        if code == product['제품번호']:
            print_product_info(product)
            break
    else:
        print("[%s] 제품코드에 해당하는 제품 정보가 없습니다." % code)

def modify_product():    
   
    code = input_info('수정')
    
    # 수정은 입력한 제품번호에 해당하는 제품의 단가와 수량을
    # 수정하도록 해야합니다.
    
    for product in inventory:
        if code == product['제품번호']:
            print("[%s] %s 제품의 가격과 수량정보를 수정합니다."
                  % (product['제품번호'], product['제품명']))
            
            product['단가'] = int(input("수정할 가격: "))
            product['수량'] = int(input("수정할 수량: "))
            product['제품총액'] = product['단가'] * product['수량']
            print("\n %s의 정보수정이 정상 처리되었습니다."
                  % product['제품명'])
            break
    else:
        print("[%s] 제품코드에 해당하는 제품 정보가 없습니다." % code)
            
def delete_product():
    
    code = input_info('삭제')
    
    # 삭제는 리스트에서 사전데이터를 제거하여 
    # 삭제가 완료된 제품의 조회가 불가능하도록 만들어야 합니다.
    for product in inventory:
        if code == product['제품번호']:
            print("[%s] %s 제품의 정보를 삭제합니다."
                  % (product['제품번호'], product['제품명']))
            
#           inventory.remove(product)             
            del(inventory[inventory.index(product)])
            print("\n %s의 삭제가 정상 처리되었습니다."
                  % product['제품명'])
            break
    else:
        print("[%s] 제품코드에 해당하는 제품 정보가 없습니다." % code)


inventory = []

while True:
    
    menu = show_menu()
    
    if menu == 1:
        reg_product()
    elif menu == 2:
        show_all_product()
    elif menu == 3:
        search_product()
    elif menu == 4:
        modify_product()
    elif menu == 5:
        delete_product()
    elif menu == 6:
        print("프로그램을 종료합니다.")
        break
    else:
        print("메뉴를 잘못 입력했습니다.")
    
    
    
    
    
    
