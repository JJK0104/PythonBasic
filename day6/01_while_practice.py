'''
1~10까지의 합 구하기
가능한 모든 걸 변수화 시키는 습관 들이기!!

sum=1
sum=1+2   / sum + 2
sum=1+2+3 / sum + 3
sum=1+2+3+4 / sum + 4
sum=1+2+3+4+5 / sum + 5
sum=1+2+3+4+5+6 / sum + 6
sum=1+2+3+4+5+6+7 
sum=1+2+3+4+5+6+7+8
sum=1+2+3+4+5+6+7+8+9
sum=1+2+3+4+5+6+7+8+9+10

a=!
a=!+@ / a+@
a=!+@+# / a+#
a=!+@+#+$ / a+$
a=!+@+#+$+%
a=!+@+#+$+%+^
a=!+@+#+$+%+^+&
a=!+@+#+$+%+^+&+*
a=!+@+#+$+%+^+&+*+()



sum = 0 
n = 1

if n <= 10 :
    sum = sum + n
    n = n + 1
if n <= 10 :
    sum = sum + n
    n = n + 1
if n <= 10 :
    sum = sum + n
    n = n + 1
if n <= 10 :
    sum = sum + n
    n = n + 1
'''

# 1~10까지의 누적합계를 구하는 로직
sum = 0 # 얜 제어 변수가 아니다
n = 1 # 제어변수(begin)
while n <= 10: # 조건식(end)
    sum += n 
    n += 1 # 증감식(step) : 증감식은 반복문을 실행하고 마지막에 나와야됨

print("1~10까지의 누적합:", sum)

# 7 ~ 100까지의 7의 배수 가로로 모두 출력하기
n = 7 
while n <= 100:
    print(n, end=" ")
    n += 7
print() # 줄개행만 하라는 명령

# 1 ~ 100까지의 8의 배수 가로로 모두 출력하기
n = 1
while n <= 100:
    if n % 8 == 0:
        print(n, end=" ")
    n += 1
print()


# 1~100까지의 정수 중 6의 배수이면서 
# 12의 배수가 아닌 수를 모두 가로로 출력하세요.
print("-" * 40)
n = 1
while n <= 100:
    if (n % 6 == 0) and (n % 12 != 0):
        print(n, end=" ")
    n += 1 # 이건 if 소속이 아니라 while 소속. 들여쓰기로 소속 확실히 하자
print()
   
# 1 ~ 9876사이의 정수 중 13의 배수의 개수를 출력
print("-" * 40)  
   
count = 0
n = 1
while n <= 9876:
    if n % 13 == 0:
        count += 1
    n += 1
print("13의 배수의 개수:", count)  



   


   