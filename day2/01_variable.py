

# 파이썬에서는 문장의 끝에 세미콜론을 사용할 수 있지만
# 권장하지 않는다
# print 2개를 한줄에 쓸 때는 세미콜론 사용해야한다
print('hello1') ; print('hi1') # hi1은 다음 줄에 나온다
print('hello','I\'m',"jjk") # hello I'm jjk
# print는 디폴트로 print(sep=" ",end="\n")이 있는거다


print('hello2') ; 
print('hi2')

'''
* 변수(variable)

1. 변수는 데이터를 저장하기 위한 공간에 이름을 붙여둔 것입니다.
2. 하나의 변수에는 하나의 데이터만 저장할 수 있습니다.
3. 변수의 값은 실행 중에 언제든지 변경할 수 있습니다.
'''
print("실행 테스트!")
a = 10 + 9
print(a)

a = 100
print(a)

print("-----------------------")

n1 = 15
n2 = 3
result = n1 * n2   #result =45
print(result)

n2 = 5
# 기본적으로 프로그램 코드는 위에서 아래로 순차적으로
print(result)    #n1 = 15, n2 = 5, result는 여전히 45
result = n1 * n2
print(result)

apple = "사과" # 따옴표를 빼면 사과 라는 변수의 값을 apple에 저장. 근데 사과라는 변수가 없으니
print(apple)




