

'''
* 중첩 반복문

- 반복문 안에는 또 다른 반복문이 들어가서 중첩 형태의 반복문을
  구성하는 것이 가능합니다.

- 반복 상황 내에서 또 다른 반복문을 실행하는 구조입니다.

- 중첩루프 작성시 주의점은 들여쓰기에 주의하여 해당실행코드가
  어떤 반복문의 실행문인지를 잘 구분해야 합니다.
'''
'''
for dan in range(2, 10, 1):
    print("* 구구단", dan, "단")
    print("=" * 40)
    
    for hang in range(1, 10, 1):
        print(dan,"x",hang,"=",dan*hang)    
    print("=" * 40)
'''

# for은 제어변수가 for과 같은 라인에 
# while은 제어변수 dan이 while 위로 나와야 된다. 
dan = 2
while dan < 10:
    print("* 구구단", dan, "단")
    print("=" * 40)
    hang = 1 #제어변수 hang은 while 위에 
    while hang < 10:
        print(dan,"x",hang,"=",dan*hang)  
        hang += 1 #증감식은 반복 실행할 코드가 끝난뒤에!!
    print("=" * 40)
    dan += 1  #증감식은 반복 실행할 코드가 끝난뒤에!!

# 삼각형 별 피라미드 그리기

# 이런 거 할 때는 logic을 생각해라. 간단한 그림을 그려 생각
# 가능한 모든 걸 변수화 시키는 습관 들이기!!
# 그리고 그 변수들간의 관계를 생각하기

'''
*
**
***
****
*****

for x in range(1,6):
    print('*'*x)

'''
# x = 1 일 때 y는 ?
# x = 2 일 때 y는 ?
# x = 5 일 때 y는 ?
print()
print("-" * 40)
for x in range(1, 6): #바깥쪽 for문은 층수를 바꾸는 역할
    for y in range(x): #안쪽 for문은 별 개수/ range(x) = range(0,x) -> 0부터 x-1까지
        print("*", end="")
    print()

#위 문제를 한번 "****" ="*"+"*"+"*"+"*"로 해석해서 해봐라

'''
***** 
****
***
**
*
'''
# x = 1 일 때 (별 개수)y는 ?
# x = 2 일 때 (별 개수)y는 ?
# x = 5 일 때 (별 개수)y는 ?
print("-" * 40)
for x in range(1, 6):
    for y in range(6-x):
        print("*", end="")
    print()

'''
    *
   **
  ***
 ****
*****
'''  
# x = 1 일 때 (공백 개수)y1는, (별 개수)y2는 ?
# x = 2 일 때 (공백 개수)y1는, (별 개수)y2는 ?
# x = 5 일 때 (공백 개수)y1는, (별 개수)y2는 ?

'''
for x in range(1,6):
    print(' '*(5-x)+'*'*x)
'''


print("-" * 40)
for x in range(1, 6):
    for y1 in range(5-x):
        print(" ", end="")
    for y2 in range(x):
        print("*", end="")
    print()

'''
*****
 ****
  ***
   **
    *
'''
'''
줄번호(x)  별개수(y) = 6-x  공백개수(z) = x -1
1            5           0
2            4           1
3            3           2
4            2           3
5            1           4
                y + z = 5
                x,y,z 모두 x로 표현 가능 -> x만의 반복문으로도 가능
'''
print("-" * 40)
for x in range(1, 6):
    for y1 in range(x-1):
        print(" ", end="")
    for y2 in range(6-x):
        print("*", end="")
    print()

print("다른 방법")
for x in range(1,6):
    
    print(' '*(x-1),end='')
    print('*'*(6-x))
'''
    *
   ***
  *****
 *******
*********
'''
print("-" * 40)
for x in range(1, 6):
    for y1 in range(5-x):
        print(" ", end="")
    for y2 in range(2*x-1):
        print("*", end="")
    print()

'''
*         *
**       **
***     ***
****   ****
***** *****


줄번호(x)    별개수(y)     공백(z)
1               2           9
2               4           7   
3               6           5
4               8           3
5              10           1
             = x*2          = 11 -2*x

근데 가능한 모든 걸 변수화 시켜보자 별개수 -> 왼쪽 별개수y1, 오른쪽 별개수 y2

줄번호(x)    왼별(y1)    오른별(y2)    공백(z)
1               1           1           9
2               2           2           7   
3               3           3           5
4               4           4           3
5               5           5           1
               =X          =X            = 11 -2*x
'''
for x in range(1,6):
    print("*"*x,end='')
    print(' '*(11-2*x),end='')
    print("*"*x)

print('다른 방법')
for x in range(1,6):
    for y1 in range(x):
        print('*',end='')
    for z in range(11-2*x):
        print(' ',end='')
    for y2 in range(x):
        print('*',end='')  
    print()
'''
0 : 0 0 0 0 
1 : 1 2 3 4
2 : 2 4 6 8
3 : 3 6 9 12
4 : 4 8 12 16
'''
# 방법 1 : 0*1 0*2 0*3 0*4 로 해석한 경우
print("방법 1 : 0*1 0*2 0*3 0*4 로 해석한 경우")
for x in range(0,5):    
    print(x,":",end = " ")
    for y in range(1,5):
        print(x*y,end = " ")
    print()

'''
4
4+4
4+4+4
4+4+4+4
'''
a=0  #a는 제어변수가 아니다...
for x in range(1,5):
    a=a+4
    print(a)
    


# 방법 2 : 0 0+0 0+0+0 0+0+0+0 으로 해석한 경우



print("방법 2 : 0 0+0 0+0+0 0+0+0+0 으로 해석한 경우")
for x in range(0,5):    
    print(x,":",end = " ")
    a = 0
    for y in range(1,5):
        a = a + x
        print(a,end=" ")
    print()

