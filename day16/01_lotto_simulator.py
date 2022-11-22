# 6개 다 맞추면 1등
# 5개 맞추면 2등 or 3등
# 5개 맞추고 보너스 번호까지 맞추면 2등
import random


win = []
bonus_num = 0

while len(win) < 6:
    num = random.randint(1, 45)
    if num not in win:
        win.append(num)

# 보너스 번호는 앞 6개와는 다른 번호
while True:
    bonus = random.randint(1, 45)
    if bonus not in win:
        bonus_num = bonus
        break                 

prz1 = 0
prz2 = 0
prz3 = 0
prz4 = 0
prz5 = 0
prz_no = 0
paper = 0 # 산 로또 개수
my_lotto = [] 

while True:

    cnt = 0 # 당첨 숫자 개수를 저장할 변수 
    num = random.randint(1, 45)  # 23

    if num not in my_lotto:
        my_lotto.append(num) # [23]

    if len(my_lotto) == 6: # my_lotto 요소 개수가 6개 될때까지 이 큰 if문은 실행 안된다
        paper += 1 #로또 몇개 산지... 맨 밑에 my_lotto.clear()로 비워지니까 my_lotto 요소 6개 될때마다 1개 구매취급

        for n in my_lotto:
            for w in win:
                if n == w:
                    cnt += 1           

        if cnt == 6: # 1등
            prz1 += 1
        elif cnt == 5: # 2등 or 3등
            if bonus_num in my_lotto: #2등
                prz2 += 1
            else:
                prz3 += 1
        elif cnt == 4:
            prz4 += 1
        elif cnt == 3:
            prz5 += 1
        else:
            prz_no += 1

        print("\n로또 %d장 구매..." % paper)

        print("="*50)

        print("당첨 횟수    당첨시 수령액(세후,평균)    누적 당첨금        당첨 확률")

        print("1등: %d번    %d원                  %d원                %.5f%%" 
              % (prz1,1500000000,prz1*1500000000,(prz1/paper)*100))
        print("2등: %d번    %d원                      %d원                %.5f%%" 
              % (prz2,40000000,prz2*40000000,(prz2/paper)*100))
        print("3등: %d번    %d원                        %d원                %.5f%%" 
              % (prz3,1000000,prz3*1000000,(prz3/paper)*100))
        print("4등: %d번    %d원                          %d원        %.5f%%" 
              % (prz4,50000,prz4*50000,(prz4/paper)*100))
        print("5등: %d번    %d원                          %d원        %.5f%%" 
              % (prz5,5000,prz5*5000,(prz5/paper)*100))
        print("꽝: %d번        0원                          0원                %.5f%%" 
              % (prz_no,(prz_no/paper)*100))
        print("="*50)

        use = paper*1000
        print("누적 사용 금액: %d원" % use)
        summ = prz1*1500000000 + prz2*40000000 + prz3*1000000 + prz4*50000 + prz5*5000

        print("누적 당첨금 총합: %d원" % summ)

        subt = summ-use
        print("순이익: %d원" % subt)
        print("수익률: %.2f%%" % ((subt / use)*100))
        print("="*50)          

        my_lotto.clear()         
        
        '''
        1등 당첨될 때까지 시행하는 코드 근데 이러면 절대 안 끝나니까 확률적으로
        if prz1 == 1:
            break
        '''
        
        if prz_no == 10:
            break
        
        
        
        