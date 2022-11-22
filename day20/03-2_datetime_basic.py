


'''
* 표준 모듈 datetime

- 현재 운영체제의 날짜 정보를 파이썬으로 읽어들이는 기능을
  제공하는 모듈입니다.
'''
# datetime 모듈에서 class datetime import하기
# 사실 class를 import 하는 게 아니라 class 정보가 담긴 객체 변수를 로딩한 거
from datetime import datetime

# 오늘 날짜정보를 담고 있는 객체를 리턴하는 법
date = datetime.today() # today라는 매서드 사용
year = date.year # date의 셀프 변수인 year
month = date.month
day = date.day
hour = date.hour
minute = date.minute
second = date.second

print("지금은 %d년 %d월 %d일 %d시 %d분 %d초입니다."
      % (year, month, day, hour, minute, second))






