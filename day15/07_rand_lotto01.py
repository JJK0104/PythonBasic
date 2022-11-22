'''
day 15-6

# 리스트의 정렬
list1 = [14, 66, 23, 77, 34, 99]
# 리스트를 오름차정렬할 때는 sort()메서드를 사용합니다.
list1.sort()
print(list1)

# 내림차 정렬시에는 sort()의 인수값으로 키워드인수 reverse=True
# 를 적어줍니다.
list1.sort(reverse=True)
print(list1)
'''

# 리스트나 집합에 로또번호 6개를 랜덤으로 담아서
# 오름차 순으로 출력하세요. 
# 단, 중복 숫자는 배제하세요. 로또번호는 1~45번입니다.
import random as r
import time

# lotto = set()으로 만들면 중복 숫자 나와도 된다
# 그리고 len(lotto) == 6 일때 리스트로 만들어주고 break 하면 됨

lotto = []

while True:    
    num = r.randint(1, 45)    
    # num을 리스트에 저장
    # 단, 해당 숫자가 리스트 내부에 없을 때만 저장
    if num not in lotto:
        lotto.append(num)
        
    if len(lotto) == 6:
        break
    
# 리스트 오름차 정렬
lotto.sort()
print("-----이번주 로또번호-----")
print(lotto)


# 당첨 번호를 생성
win = set()

while len(win) < 6:
    num = r.randint(1, 45)
    win.add(num) # set 관련 함수는 day11

# set은 정렬 못 한다
# 그래서 set을 list로 바꾸고
win = list(win)
win.sort()

print("로또번호 추첨을 시작합니다.")
for n in win:
    print(n, end=" ")
    time.sleep(.6)
print()

time.sleep(2)
if win == lotto:
    print("1등 당첨")
else:
    print("당첨 실패!")









