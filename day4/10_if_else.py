
'''
* if ~ else

- if블록이 조건식의 결과가 True일 경우에만 실행된다면
  else블록은 '위의' if의 조건식의 결과에 따라 값이 False일 
   경우에 실행됩니다.
  
  ex) if 조건식1:
      if 조건식2:
      else :
      이라면 else는 조건식2의 예외 경우만 실행됨. 조건식1의
      True/False와는 무관



- if뒤에는 반드시 논리값을 반환하는 조건식을 적어야 하지만
  else뒤에는 아무것도 적지 않습니다.

- if는 단독사용이 가능하지만 else는 반드시 if와 함께 사용해야
  합니다.
'''

money = int(input("얼마 있냐?? "))

if money >= 20000:
    print("치킨 시켜먹자!!")
    print("신나는 치킨파티 >_<")
else:
    print("그냥 라면이나 먹어야지 ㅠㅠ")
print("야식은 적당히~~")


print("")
if money > 20000:
      print("치킨 시켜먹자")
if money == 20000:
      print("20000원이 있다")
else : 
    print("라면 먹자") # 위 print랑 띄어쓰기 달라도 되네

# 위의 else는 money 가 20000이 아닐 경우에 실행됨
# 따라서 money가 21000이면 첫번째 if와 else가 실행됨


print("")
if money > 20000:
    print("치킨 시켜먹자")
elif money == 20000:
    print("20000원이 있다")
else : 
    print("라면 먹자") 

# money가 21000이면 첫번째 if만 실행된다