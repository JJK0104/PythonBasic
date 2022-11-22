


import random as r

# 당첨번호 생성
win = set()
while len(win) < 6:
    num = r.randint(1, 45)
    win.add(num)

win = list(win)
win.sort()

# 내가 구매할 로또를 1등이 당첨될 때까지 구매하는 로직 작성.

cnt = 0
while True:
    
    my_lotto = set()
    while len(my_lotto) < 6:
        num = r.randint(1, 45)
        my_lotto.add(num)
    my_lotto = list(my_lotto)
    my_lotto.sort()  
    cnt += 1
    
    if my_lotto == win:
        print("1등에 %d번만에 당첨되셨습니다. 축하합니다!!"
              % cnt)
        print("당첨까지 사용한 금액: %d원" % (cnt * 1000))
        print("당첨확률: %.8f" % ((1/cnt) * 100))
        break
    else:
        print("로또 %d장째 구매중..." % cnt)
    





