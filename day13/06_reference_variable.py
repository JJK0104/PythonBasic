a = 3
b = a
print('a: %d, b: %d' % (a, b)) # a: 3, b: 3

a = 5
print('a: %d, b: %d' % (a, b)) # a: 5, b: 3


list1 = [1,2,3]
list2 = list1

print("list1:", list1) # list1: [1, 2, 3]
print("list2:", list2) # list2: [1, 2, 3]

list2[1] = 100 

#list2의 1번 인덱스를 바꿨더니 list1의 1번 인덱스도 똑같이 바뀜
print("list1:", list1) # list1: [1, 100, 3]
print("list2:", list2) # list1: [1, 100, 3]

print("list1의 주소값:", id(list1)) # list1과 list2의 주소값이 똑같다
print("list2의 주소값:", id(list2))


'''
* 리스트 사본 만들기

- 수치형 변수는 저장 공간이 서로 독립적이라 대입하면 일시적으로
  값이 같아질 뿐 둘 중 하나를 변경한다해도 다른 변수에는 영향을
  주지 않습니다.

- 그러나 리스트와 같은 객체데이터(집합데이터 같은 것들)는 하나의 리스트를 다른 리스트에
  대입하면 2개의 리스트가 동시에 영향을 받게 되는데  그 이유는 
  2개의 리스트가 독립된 형태가 아닌 같은 메모리 주소값을 공유하고
  있기 때문입니다.

- 리스트의 독립적인 사본을 얻으려면 리스트의 메서드 copy()를
  사용합니다. 
  메서드는 .copy() 처럼 앞에 .을 붙이고 사용한다
'''
print("-" * 40)

list1 = [4,5,6] 
list2 = list1.copy()

print("list1:", list1)
print("list2:", list2)

list2[1] = 100
list1[2] = 200

print("list1:", list1)
print("list2:", list2)
print("list1의 주소값:", hex(id(list1)))
print("list2의 주소값:", hex(id(list2)))






