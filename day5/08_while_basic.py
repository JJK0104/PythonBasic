
# 반복문은 위에서 아래로 '순차적'으로 진행 !!

'''
* 반복문(Loop)

- 반복문은 유사한 명령을 반복해서 실행하는 제어문입니다.
- 파이썬의 반복문 키워드는 while, for가 있습니다.

* while

제어변수 선언(begin)
while 논리형 조건식(end):
       반복 실행할 코드
       제어변수의 증감식(step)

- 제어변수란 반복문의 반복횟수를 제어할 변수입니다.
'''



n = 1

if n <= 10:
    n = n + 1 
    print(n, "번 성적처리 완료!")
if n <= 10:
    n = n + 1 
    print(n, "번 성적처리 완료!")
if n <= 10:
    n = n + 1 
    print(n, "번 성적처리 완료!")
if n <= 10:
    n = n + 1 
    print(n, "번 성적처리 완료!")



print("="*30)

#while문 구조를 잘 봐라
#제어변수 설정은 while문 바로 밖(위)
#제어변수 증감식은 반복 실행할 코드 아래에 

stu_num = 2 # 제어변수 선언

while stu_num <= 10: # 논리형 조건식
    print(stu_num, "번 성적처리 완료!") # 반복 실행할 코드
    stu_num += 2  # 제어변수의 증감식 : 반복 실행할 코드가 끝난 뒤에 와야됨.

# print(stu_num)

print()
print("="*40)

#제어변수 선언, 증감식 위치 주목 

n=1 #제어변수 선언... while문 밖(위)에
while n <=9 : 
    print("구구단 {}단".format(n))
    print("="*40)
    s=1  # 제어변수 선언... s는 2차while을 제어하는 변수니까 2차 while 위에 설정
    while s <= 9 : 
        print("{}X{}={}".format(n,s,n*s))
        
        s = s + 1

    n = n + 1



#구구단 출력

n = 1
while n <= 9 :
    print(str(n), "\b단")
    print("="*10)
    
    s = 1
    while s <= 9:
        print(str(n),"*",str(s),"=",str(n*s))
        s = s + 1

    n = n + 1
