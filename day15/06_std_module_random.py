'''
* 표준 모듈 random

- 프로그램이 무작위 동작을 하게 하려면 랜덤값이 필요합니다.

- 랜덤값을 난수라고 하며 난수를 쉽게 발생시킬 수 있도록 함수를
  지원하는 모듈이 random모듈입니다.

- random모듈의 random()함수는 0.0이상 1.0'미만'의 '실수' 난수값을
  발생시킵니다.
'''
import random as r

rn = r.random()
print("랜덤값:", rn)

print("오늘 저녁을 뭘 먹을까영??")

if rn > 0.8:
    print("치킨에 맥주를 먹자!!")
elif rn > 0.6:
    print("닭발에 소주 고고씽~~")
elif rn > 0.4:
    print("집에서 라면이나 먹는거야~~")
elif rn > 0.2:
    print("답은 보쌈셋트다!!")
else:
    print("그냥 굶어!")


'''
- 정수 난수는 randint()함수를 사용합니다.
- randint()는 인수로 시작범위와 끝범위를 지정하는데
  끝범위도 난수값에 포함되는 특징이 있습니다. 파이썬에서
  98%는 이상 미만 인데 이건 2%에 든다
'''
pet = ['멍멍이', '야옹이', '타란튤라', '비둘기', '소라게']

ri = r.randint(0, 4)
print("애완동물을 뭘 키울까??", pet[ri])


# 리스트의 정렬
list1 = [14, 66, 23, 77, 34, 99]
# 리스트를 오름차정렬할 때는 sort()메서드를 사용합니다.
list1.sort()
print(list1)
print(list1.sort()) # None이 출력된다. sort 쓸때는 list1.sort 입력해주고 그냥 print(list1) 하는 건가
# 내림차 정렬시에는 sort()의 인수값으로 키워드인수 reverse=True
# 를 적어줍니다.
list1.sort(reverse=True)
print(list1)








