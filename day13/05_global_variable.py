

'''
* 전역 변수(global variable)

- 지역변수가 함수 내부에서만 사용되는 변수라면 전역변수는
  프로그램 전체에서 사용되는 공용변수입니다.

- 파이썬에서는 들여쓰기 없이 선언된 변수가 전역변수로 취급되며
  함수 내부, 제어문 내부 등 프로그램 어디에서나 사용이 가능합니다.
'''
def calc_price(price):
    print("오늘의 할인율:", sale_rate)
    
    today_price = price * sale_rate # 지역변수
    print("오늘의 가격:", today_price)
    print("-" * 40)

sale_rate = 0.8 # 전역변수 , * 원래 파이썬은 아래에 만들면 위에는 적용 안됨 
                # 근데 이렇게 아래에 적는 이유는 
                # 위 함수가 바로 실행되는 코드가 아니기 때문. 
                # 함수가 호출되어야 실행되기 때문에 

# print(today_price) today_price는 지역변수다
# print(price) price 역시 지역변수다

calc_price(1000) # 전역변수인 sale_rate = 0.8 사용
sale_rate = 0.7
calc_price(1000) # 바뀐 전역변수인 sale_rate = 0.7 사용

print()
print()

price = 1000 # 전역변수

def exam():
      # 함수 내부에서는 똑같은 이름의 지역변수, 전역변수가 있을 경우 
      # 전역변수보다 지역변수를 우선 사용한다
      price = 400
      print(price) # 지역변수 price 출력

exam() # 400 지역변수 price 출력 
       # 그리고 출력한다음에 지역변수는 메모리상 사라지고 전역변수 price만 남아있다
print(price) #1000 전역변수 price

print()
print()
def sale():
    # 함수 내부에서는 전역변수보다 지역변수를 우선 사용합니다.
    
    global price # 함수 내부에서 전역변수 price를 사용해라!
    #앞으로 이 함수에서는 price는 전역변수라는 걸 지칭해주는 거다
    
    price = 500
    print('지역변수 price의 주소값:', id(price))

sale()

print('전역변수 price의 주소값:', id(price))
print(price)

print()



