


'''
* 인수 (arguments)

- 인수는 함수를 호출할 때 함수 실행에 필요한 값들을 전달하는 매개체이며,
  그렇기 때문에 매개 변수(parameter)라고도 부릅니다.

- 함수 호출부에서 어떤 인수값을 전달하느냐에 따라 함수의 실행 결과가
  달라집니다.

- 인수의 개수는 제한이 없어 많은 값을 함수에 전달할 수도 있고, 하나도
  전달하지 않을 수도 있습니다.

- 함수를 정의할 때 지정한 인수의 수만큼 호출할 때도 동일한 수의 인수값을
  전달해야 합니다.

- 인수의 이름을 지어줄 때는 아무렇게나 지어도 무방하지만 이 함수를 처음
  사용하는 사람도 인수 이름만 보고 무슨 값을 전달해야 할지 의미를 알기 쉽게
  지정하는 것이 좋습니다.
'''
def get_items(weapon, armor):
    
    w = "'%s' 무기를 획득했습니다." % weapon
    ar = "'%s' 방어구를 획득했습니다." % armor
    detail = w + "\n" + ar + "\n-------------------------"
    return detail

print(get_items('단검', '철갑옷'))
'''
C언어 기억부류(지역변수, 전역변수)식 해석

get_items함수를 만났으니 위로 가서 get_items함수를 찾아보니 해당함수가 있다. 그래서 해당 함수를 사용
그럼 '단검', '철갑옷'이 get_items에 전달 될 거고 그곳에서 함수를 실행한다
   
    w = "'%s' 무기를 획득했습니다." % weapon
    ar = "'%s' 방어구를 획득했습니다." % armor
    detail = w + "\n" + ar + "\n-------------------------"
    return detail

그리고 이 get_items함수가 종료되면 위 지역변수들은 수명을 함수와 함께하면서
함수가 종료되면서 지역변수들도 사라짐
이제
print(w) 
print(detail) 
라고 치면 변수가 없어서 오류가 뜬다

함수가 실행중일 때는  
w = "'%s' 무기를 획득했습니다." % weapon
detail = w + "\n" + ar + "\n-------------------------"
이라는 변수들이 있었지만 get_items함수가 종료되면서 같이 사라짐, 지역변수라서

'''

print(get_items('누더기옷', '활'))

# 인수를 전달받지 않는 함수의 예
def calc_sum10():
    sum = 0
    for n in range(1, 11):
        sum += n
    return sum

# calc_sum10() 
# print(sum)
# 위에 두 코드 입력하면 오류뜬다...
# sum이라는 변수가 없으니까, sum은 calc_sum10()이 종료되면서 같이 없어지는 지역변수다(?)
print(calc_sum10())
print(calc_sum10())




