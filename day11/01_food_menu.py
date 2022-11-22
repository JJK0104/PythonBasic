

# 음식점 메뉴판 관리 프로그램
# key: 메뉴명, value: 가격

'''
# 내부에 뭐라도 써놔야 된다
# 쓸게 없으면 pass 라도 써라
menu = input("=> ")

if menu == 1:
    pass
elif menu == 2:
    pass
elif menu == 3:
    pass
else :
    pass

'''


foods = {}

while True:
    print("\n========음식점 메뉴 관리 프로그램========")
    print(" 1. 신규 메뉴 등록하기")
    print(" 2. 메뉴판 전체보기")
    print(" 3. 프로그램 종료하기")
    print("===================================")
    menu = input("=> ")
    
    if menu == "1":
        # 1. 메뉴명을 입력받아 해당메뉴가 사전에 이미 존재한다면
        #    "이미 등록된 메뉴입니다"를 출력하세요
        # 2. 사전에 존재하지 않는 메뉴(key)라면 가격을 입력받아
        #    key:value쌍으로 맵핑하여 사전에 저장하세요. 
        name = input("메뉴명: ")
        
        if name not in foods:
            price = input("가격: ")
            foods[name] = price
            print("신규 메뉴 %s(이)가 등록되었습니다." % name)
#             print(foods)
        else:
            print("%s(은)는 이미 등록된 메뉴입니다." % name)
     
        
        
    elif menu == "2":
        print("\n-------------메뉴판----------------")
        for m in foods:
            print("%s : %s원" % (m, foods[m]))  
        
        print("----------------------------------")    
        print("1. 수정 | 2. 삭제 | 3. 나가기")
        select = input("=> ")
        
        if select == "1":
            print("가격을 변경할 메뉴의 이름을 입력하세요.") #딕셔너리는 key는 못 바꾸고 value만 바꿀 수 있다
            name = input('=> ')
            
            if name in foods:
                newprice = input("변경할 가격: ")
                foods[name] = newprice
                print("%s의 가격이 %s원으로 변경되었습니다."
                      % (name, newprice))
            else:
                print("%s는(은) 등록된 메뉴가 아닙니다."
                      % name)
            
        elif select == "2":
            print("삭제할 메뉴명을 입력하세요.")
            name = input("=> ")
            if name in foods:
                del(foods[name])
                print("%s이(가) 삭제되었습니다." % name)
            else:
                print("%s는(은) 등록된 메뉴가 아닙니다."
                      % name)
            
        elif select == "3":        
            continue # while True 로 올라간다
        
    elif menu == "3":
        print("프로그램을 종료합니다.")
        break # while True 탈출
    else:
        print("메뉴를 잘못 입력했습니다.")





