

'''
* 반복문 for

- for문은 시퀀스 자료형 내의 데이터를 순차적으로 꺼내서 반복 작업하는
  반복문입니다.

- 시퀀스 자료형이란 여러 개의 값들을 모아놓은 집합이며 대표적으로 리스트,
  문자열 등이 있습니다.

- 리스트란 []안에 데이터들을 나열해 놓은 일종의 배열입니다.

ex) for 제어변수 in 시퀀스 자료형 데이터:
            반복 실행할 코드
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(nums)) # <class 'list'>

for stu_num in nums:
    print(stu_num, "번 학생 성적처리!!")

print("-" * 40)
sum = 0
for n in nums:
    sum += n
print("1~10까지의 누적합:", sum)


'''
* 내장함수 range(begin, end, step) : 특정 범위의 순차적 리스트를 생성하는 함수

- 순차적으로 증가하는 정수 리스트를 만들 때 대괄호 안에 데이터를
  콤마로 일일히 나열하기보다는 range함수를 사용하여 쉽게 리스트를
   생성할 수 있습니다.

ex) range(시작값, 끝값, 증감값)
- 시작값은 포함하지만 끝값은 포함하지 않습니다.
*step이 1일 경우 생략 가능
- range(1, 5, 1) == range(1, 5) -> [1,2,3,4]
- range(3, 8, 2) -> [3,5,7]
*숫자 하나만 입력하면 그 값을 end로 보고 시작값을 0 으로 본다.
- range(6) == range(0,6,1)
'''
print("-" * 40)
a = range(1, 11, 1)
print(a) # range(1, 11)
print(type(a)) # <class 'range'>

a = list(range(1, 11, 1))
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(range(4, 15)) # 증감값 생략시 1로 처리
print(b) #[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

c = list(range(1, 11, 3))
print(c)

# range에 값을 하나만 주면 끝값으로 처리, 시작값을 0으로 처리
d = list(range(6)) # range(0, 6, 1)
print(d)

# 1~100까지의 누적합계를 구하는 for문의 사용 예
sum = 0
n = 1 #제어변수 begin
while n < 101:#조건식 end
    sum += n
    n += 1 #증감식 step
print("1~100까지의 누적합:", sum)

#위의 제어변수, 조건식, 증감식을 아래에도 적용해보자

sum = 0
for n in range(1, 101, 1): #n은 제어변수, 1이 begin, 101이 end, 1이 step
    sum += n
print("1~100까지의 누적합:", sum)

print("-" * 40)
print("1부터 100까지의 8의 배수 가로로 출력 : ")
for n in range(1, 101):
    if n % 8 == 0:
        print(n, end=" ")
print()

print("-" * 40)  
count = 0
for n in range(1, 9877):
    if n % 13 == 0:
        count += 1
print("13의 배수의 개수:", count)  

# 정수 x와 y를 입력받아 x부터 y까지의 
# 누적합을 처리하는 코드를
# for문과 range()를 사용하여 구성해보세요.
print("-" * 40)

sum = 0
x = int(input("정수 x 입력: "))
y = int(input("정수 y 입력: "))
for n in range(x, y+1):
    sum += n
print(x,"부터", y,"까지의 누적합:", sum)









