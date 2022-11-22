
'''
* while 연습
- 정수를 하나 입력받아 1부터 입력받은 정수까지의 
누적합계를 while을 사용하여 구하는 코드를 만드세요. 
ex) 출력 예시: "1부터 x까지의 누적합계: y"
'''
sum = 0
n = int(input("정수1 입력: ")) # 제어변수(begin)
x = int(input("정수2 입력: "))

if n > x:

#n,x 값을 서로 바꾸는 과정
#     t = n   등호는 우측을 좌측에 대입하는 거다. 즉 좌측에는 무조건 이미 존재하는 변수가 와야된다
#     n = x
#     x = t
    n, x = x, n  # 위 과정을 간단히 한거. python에서만 가능.

n2 = n
while n <= x: # 조건식(end)
    sum += n 
    n += 1 # 증감식(step)

print(n2, "~", x,"까지의 누적합:", sum)

'''
#1부터 X값까지의 합
# 1 + 2 + 3 + 4 + ... + X = Sum 형식으로 출력
# 1부터 X까지의 합은 Sum 입니다로 출력
'''
num = int(input("정수 값을 입력하세요 : "))

sum = 0
n = 1 
while n <= num : 
    sum = sum + n
    print(n, end = " + ")
    n = n + 1
print("\b\b=", sum)

#print("1부터 {}까지의 합은 {}입니다".format(num,sum))


'''
두 정수를 입력받아 X부터 Y 까지의 합 구하기
'''
print()
print("두 정수를 입력받아 X부터 Y 까지의 합 구하기")

num1 = int(input("정수1를 입력하세요 : "))
num2 = int(input("정수2를 입력하세요 : "))

if num1 > num2 : 
    bn = num1
    sn = num2
elif num1 == num2:
    bn = num1
    sn = num1
else : 
    bn = num2
    sn = num1

# #sn부터 bn까지의 합은 {} 입니다
# #sn + (sn+1) + --- + bn

# sn = []
# sum = sn

# sn = sn + 1 
# sum = sum + sn

# sn = sn + 1 
# sum = sum + sn

# until sn = bn... = if sn<=bn

sum = 0
while sn <= bn : 
    print(sn,end = " + ")
    sum = sum + sn
    sn = sn + 1
print("\b\b=", sum)   
    















