
'''
* 다중 분기 조건문 if ~ elif ~ else

- 조건 분기를 여러 개 설정하고 싶다면 if블록 아래에
  elif라는 키워드를 쓰고 새로운 조건을 설정합니다.

- 시작 if문의 조건식의 결과가 False일 경우 아래에 있는
  elif의 조건식을 새롭게 테스트하여 해당 조건이 True일
   경우 elif의 종속된 코드를 실행합니다.

- elif문을 여러 개 쓰는 것도 가능합니다.

- if ~ elif문에서 주의사항은 조건식을 위에서부터 차례대로
   검사하면서 내려오므로 조건 설정이 중복되지 않도록 주의해야
   합니다.
'''

# 내부에 뭐라도 써놔야 된다
# 쓸게 없으면 pass 라도 써라
menu = input("=> ") # input은 str이다

if menu == 1: # 지금 menu는 str, 1은 int
    print("menu = 1")
elif menu == 2:
    pass
elif menu == 3:
    pass
else :
    pass


age = int(input("나이: "))

# 1개의 if - elif - else 
''' 시작 if문의 조건식의 결과가 False일 경우 아래에 있는
  elif의 조건식을 새롭게 테스트하여 해당 조건이 True일
   경우 elif의 종속된 코드를 실행합니다.'''
if age >= 20:     
    # 위를 age >= 12로 설정하면 아래 조건식을 삼키므로 좋지 않다. age = 12이면 age>=12 코드만
    # 실행되고 아래 코드들은 실행되지 않는다.
    print("성인입니다.")
elif age >= 17:
    print("고등학생입니다.")
elif age >= 14:
    print("중학생입니다.")
elif age >= 8:
    print("초등학생입니다.")
else:
    print("미취학 아동입니다.")


print("-"*40)
print("")
# if 3개와 if-else 1개
# age = 23 이면 첫번째 if에서 조건 판단하고 두번째 if에서 또 조건 판단하고 3번째 if에서 또 조건 판단하고
# 마지막 if - else에서 또 조건 판단해 총 4번의 조건 판단이 이루어짐
if age >= 20:
    print("성인입니다.")
if age >= 17:
    print("고등학생입니다.")
if age >= 14:
    print("중학생입니다.")

if age >= 8:
    print("초등학생입니다.")
else:
    print("미취학 아동입니다.")

