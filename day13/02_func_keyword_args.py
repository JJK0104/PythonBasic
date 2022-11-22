

'''
* 키워드 인수 (keyword arguments)

- 인수의 개수가 많아지면 인수의 순서를 잘 알기 어렵고
  함수를 사용할 때 전달할 값의 위치를 헷갈릴 가능성이 높아집니다.
  
ex) def reg_member(id, pw, name, addr, phone):

    reg_member('abc1234', 'def111', '홍길동',....)

- 파이썬에서는 순서와 무관하게 인수를 전달하는 방식을 제공하며
  인수의 이름을 직접 지정하여 대입하는 방식을 허용합니다.
'''
def calc_sum(begin, end, step):
    sum = 0
    for n in range(begin, end+1, step):
        sum += n
    return sum

print(calc_sum(3, 7, 1)) # 위치 인수값 사용

# 키워드 인수값 사용
print(calc_sum(begin=3, end=7, step=1)) # 인수의 이름을 직접 지정하여 대입하는 방식
print(calc_sum(end=7, step=1, begin=3))

# 위치인수와 키워드인수의 혼합사용( 위치인수는 항상 키워드 인수보다 먼저 나와야 한다)
print(calc_sum(3, 7, step=1)) # 3,7은 위치를 알아~ 그래서 3은 begin, 7은 end. 그리고 step은 위치 모르겠으니까 step=1
print(calc_sum(3, step=1, end=7)) # begin 자리는 아는데 step,end 자리는 기억이 안 나
# print(calc_sum(end=7, 3, 1)) # end=7 이라고 OK. 3은 end자리고 1은 step 자리네 그럼 begin은 어딨어?  

# print(sep='**', end='==>', 3, 6, 9) sep,end는 키워드 인수고 3,6,9는 위치 인수
print(3, 6, 9, sep='**', end='==>')
print(3, 6, 9, end='==>', sep='**')

'''
* 키워드 가변 인수(알고만 있어라, 자주 쓰진 않음)

- 키워드 인수는 여러개(n개) 전달해서 처리하고 싶을 때는
  인수 이름 앞에 **를 붙여 사용합니다.

- 함수 호출부에서 여러 개의 키워드 인수를 전달하면 인수의
  이름과 값의 쌍을 사전으로 만들어 함수에게 전달합니다.

- 전달 받은 사전데이터를 함수 내부에서 사용할 때는 사전의 키를
  통해 값을 참조하는 방식으로 인수값을 꺼내어 사용합니다.
'''
print()
print()
def food_na(**foods):
      print(type(foods)) # <class 'dict'>
      print(foods)

food_na(chicken="통닭",gimbap="김밥",ramen="라면") # <class 'dict'>
                                                  # {'chicken': '통닭', 'gimbap': '김밥', 'ramen': '라면'}

print()
def food_name(**foods):
    
    print("오늘 먹을 음식들~~~")
    for k in foods:
        # print(type(k)) # <class 'str'>
        print(k,':',foods[k])

food_name(chicken="통닭", gimbab="김밥", danmu='단무지', tenpura='튀김')






