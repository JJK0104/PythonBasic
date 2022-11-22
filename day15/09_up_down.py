'''
* UP & DOWN 게임
1. 1~100사이의 정수 난수를 발생시켜 해당 값을 사용자가 맞추게 
   하는 게임입니다.

2. 사용자가 처음 입력한 값이 정답값보다 큰지 작은지 사용자에게 
알려주어 사용자가 지속해서 범위를 좁혀가며 답을 찾을 수 있도록 합니다.

3. 정답을 맞췄을 때 프로그램이 종료되도록 프로그램을 구성해보세요.

4. 사용자가 정답을 맞췄을 때 몇번만에 정답을 맞췄는지 
   출력하는 로직을 추가하세요.
'''
import random

secret = random.randint(1, 100)
count = 0
count_down = 7 # 7번 안에 맞춰야함

print("[UP & DOWN 게임 - 1~100사이의 숫자 중 어떤 숫자가 들어있을까요???]")
while True:    
    print("-" * 40)
    num = int(input("숫자를 입력하세요: "))
    count += 1
    count_down -= 1
    
    if count_down <= 0:
        count_down = 0    

    if num == secret:
        if count < 8:
            print("정답입니다!! %d번만에 맞추셨군요~" % count)
            print("YOU WIN!")
            break
        else:
            print("정답입니다!! %d번만에 맞추셨군요~" % count)
            print("YOU LOSE! 원샷입니당~~ >_<")
            break
    elif num < secret:
        print("UP!!")
        print("정답 기회 %d번 남음~~" % count_down)
    else:
        print("DOWN!!")
        print("정답 기회 %d번 남음~~" % count_down)
        
 
 
 
 
        