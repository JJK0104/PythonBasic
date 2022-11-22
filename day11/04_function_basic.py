


sum = 0
for n in range(1, 6):
    sum += n
print("1~5까지의 합계:", sum)

sum = 0
for n in range(1, 11):
    sum += n
print("1~10까지의 합계:", sum)

sum = 0
for n in range(1, 101):
    sum += n
print("1~100까지의 합계:", sum)

'''
* 함수 (Function)

- 함수는 반복적으로 사용되는 코드 블록에 이름을 붙여놓은 형태입니다.

- 함수를 한번 정의해두면 지정해둔 함수 이름을 통해 언제든 해당 코드
   블록을 재사용할 수 있습니다.

- 함수를 정의할 때는 def라는 키워드를 사용합니다.

- 정의해둔 함수를 사용하는 것을 호출(call)이라고 부릅니다.

- 파이썬에서는 함수를 호출하려면 반드시 호출문 위에 함수가 
  먼저 정의되어 있어야 합니다.
'''

# 함수의 정의
def calc_sum(x):
    print("함수가 호출됨!")
    sum = 0
    for n in range(1, x+1):
        sum += n
    return sum

# 함수의 호출
print("-" * 40)
print('1~5까지의 합계:', calc_sum(5))
print('1~10까지의 합계:', calc_sum(10))
print('1~100까지의 합계:', calc_sum(100))

print("-" * 40)
result = calc_sum(5) # 함수의 호출 결과도 변수에 담을 수 있다. 
                     # 대입 연산자는 우항 연산이 우선이다. cal_sum(5)가 먼저 실행됨
                     # calc_sum(5)이 실행되면서 print("함수가 호출됨!")이 실행돼 
                     # 함수가 호출됨! 문구가 출력된다
print(result) # 얘는 return값인 15만 출력된다


print(type(calc_sum(99))) # 함수가 호출됨!
                          # <class 'int'>
                          

li = [1,2,3,4,5]
print(len(li)) # 5

# 함수의 정의
def length(x):
    count = 0
    for n in x:
        count += 1
    return count

print("-" * 40)
li = [1, 3, 5, 7, 9, 11]
print(len(li)) # 6
print(length(li)) # 6

s = "hello python"
print(len(s)) # 12
print(length(s)) # 12

'''
* 연습
1. 인수를 정수형태로 시작값(start), 
   끝값(end)을 입력받아 
   반복문으로 start부터 end까지의 
   누적 총합을 구하는 함수를 
   정의하세요.
2. 함수 이름은 calc_rangesum로 정의하세요.
ex) calc_rangesum(3, 7) ==> 
3부터 7까지의 누적합을 구해와야 함.

3. 출력예시: "x~y까지의 누적합: z"
'''
def calc_rangesum(start, end):
    sum = 0
    for num in range(start, end + 1):
        sum += num
    return sum
 
print("-" * 40)

n1 = int(input("정수1: "))
n2 = int(input("정수2: "))

print("%d~ %d까지의 누적합: %d"
      % (n1, n2, calc_rangesum(n1, n2)))

# 여기서 마지막 print("%d~ %d까지의 누적합: %d"% (n1, n2, calc_rangesum(n1, n2))) 을
# 위로 빼서 
# n1 = int(input("정수1: "))
# n2 = int(input("정수2: "))
# calc_rangesum(n1,n2)
# print("%d~ %d까지의 누적합: %d"% (n1, n2,sum))
# 하면 오류뜬다 왜냐면 sum이라는 변수가 없으니까
# return된 sum을 저장 안했으니까 sum은 함수가 종료되면서 사라짐 (?)
# 만약 저렇게 쓰고 싶으면 sum = calc_rangesum(n1,n2) 처럼 return값을 저장해야함






