

'''
* 집합 (Set)

- 집합은 여러 값들의 모임이며 저장 순서가 보장되지 않고, 
  중복값을 허용하지 않습니다.

- 집합은 사전과 마찬가지로 {}로 표현하지만 key, value쌍이 아닌
  데이터가 한개씩만 존재한다는 점이 사전과 다릅니다.

- set()함수는 공집합을 만들기도 하지만 다른 자료형을 집합으로
  변환할 수도 있습니다.

- 내장함수 set()
  s = set() #비어있는 공집합 만드는 유일한 방법

- add, remove, update
'''
names = {'허준', '신사임당', '권율', '홍길동', '허준'}
print(type(names)) # <class 'set'>
print(len(names)) # 4개다 왜냐면 중복값을 허용하지 않기 때문에
print(names) # 허준이 한번 저장돼 있고 순서도 랜덤이다, 순서가 없기 때문에 
             # {'홍길동', '권율', '신사임당','허준'}

# 내장함수 set()
s = set() #비어있는 공집합 만드는 유일한 방법
print(type(s))
'''
# 빈 튜플 만들 수 있는 유일한 방법
tu = tuple()
'''
'''
#아래처럼 만들면 빈 집합이 아니라 빈 딕셔너리다.
dic = {}
print(dic)
'''
print(set('programming')) # 순서가 랜덤이고 r,g,m 은 한번씩만 저장된다
                          # {'r', 'p', 'n', 'g', 'o', 'a', 'm', 'i'}
print(set([12, 15, 17, 11, 15])) # 저장 순서 랜덤 + 15는 한번만 저장
                                 # {17, 11, 12, 15}

dic = {'a':1, 'b':2, 'c':3}
print(set(dic)) #key만 집합으로 만들고 순서는 랜덤이다 -> {'b', 'a', 'c'}
print(list(dic)) #key만 추출 + 순서 지킨다 ->['a', 'b', 'c']

#순서는 지멋대로다
for x in {'가', '나', '다', '라'}:
    print(x)

'''
- 집합은 변경 가능한 자료형이어서 언제든지 데이터를 편집할 수 
  있습니다. (문자열, 튜플 빼고는 변경 가능)

- 집합의 요소를 추가할 때는 add()메서드를 사용하고, 제거할 때는
  remove()를 사용합니다. 결합할 때는 update()를 사용합니다.
'''
print("-" * 40)
asia = {'korea', 'china', 'japan'}
print(asia) # {'china', 'japan', 'korea'}

asia.add('thailand')
asia.add('china')
asia.add('china')
asia.add('china')
asia.add('china')
asia.add('china')
asia.remove('japan')
print(asia) # {'china', 'thailand', 'korea'}

asia2 = {'iraq', 'singapore', 'korea'}
# print(asia + asia2) 더하기 안 된다, 오류뜸
asia.update(asia2) # 중복 데이터는 하나만
print(asia) # {'singapore', 'china', 'korea', 'iraq', 'thailand'}





