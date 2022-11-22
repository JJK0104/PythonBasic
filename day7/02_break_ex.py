
'''
* 탈출문(흐름 제어문) - break, continue

- 반복문은 조건을 만족하는 동안 계속 코드를 반복하기 때문에
  한번 반복이 시작되면 반복횟수가 끝날 때까지 반복을 진행합니다.

- 하지만 중간에 어떤 이유로 반복을 중지하거나 현재 반복을 건너뛰어야
  할 경우 탈출문을 사용합니다.

* break

- break는 현재 반복문을 즉시 종료시키고 '반복문 블록'을 탈출합니다. break 밑에 거도 무시 
- break문은 for문, while문 등 반복 Loop문을 빠져 나오는 데 사용하는 구문으로
  한 번에 '가장 가까운' '하나의 Loop'를 벗어 날 때 사용한다. 
- 일반적으로 특정 조건하에서 반복문을 종료시키므로 if문과 함께
   사용합니다.
'''
for a in range(1, 11):
    if a == 6:
        print("\nbreak 위에 있기 때문에 이건 나옴")
        break
        print("이것도 안나옴나얼;ㅁ나어리ㅏ먿")

    print(a, end=" ")
print("\n반복문 종료!")

points = [92, 56, -77, 33, 48, 99]

for p in points:
    if (p > 100) or (p < 0):
        print("\n점수처리 과정에서 문제 발생! 성적을 확인하세요.")
        break
    print(p, end=" ")
print("\n점수 처리 완료!")


print("="*40)
s=1
while s<12 : 
    print("while문의 {}번째 실행".format(s))
    for x in range(1,10):
        print(x,"단")
        print("="*40)
        if x == 6:
            print("6단에서 break로 종료")
            break
        
        for y in range(1,10):
            print(x*y)
        print()
    s=s+1

