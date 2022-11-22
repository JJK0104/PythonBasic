# 미리 만든 calculator 모듈 보고 오기
# calulator 모듈에서 

''' 
* 사용자 정의 모듈

- 하나의 모듈파일에 너무 많은 코드가 들어있으면 편집이 힘들어지고
  코드를 유지보수하는 데 어려움이 생깁니다. 

- 관리 편의상 비슷한 기능을 가진 코드들을 여러 개의 파일에 나눠서
  작성하는 것이 좋습니다.
'''

#import을 하면 calculator의 print부분도 출력된다
import calculator as cal # 딱 여기까지 쓰고 ctrl+f5 누르면
                         # 1~50까지의 누적합 : 1275
                         # 메롱메롱
                         #
                         # __name__의 값: calculator 
                         # 라고 출력된다

from calculator import info # 소속 밝히기 싫으면
                            # 만약 아무것도 안 쓰고 딱 이 한줄만 쓰고 실행하면
                            # 위에 import calculator as cal만 쓴 거처럼 출력됨

# 근데 이 두개, import calculator as cal, from calculator import info 를 다 쓰면
# calculator의 print 내용물이 2번 출력되는 게 아니라 한 번 출력됨


INCH = 22
print(INCH) # 22
print("1인치: %.2fcm" % cal.INCH) # 1인치: 2.54cm
print("1~10까지의 누적합:", cal.calc_sum(10)) # 1~10까지의 누적합: 55
 
info() # 모듈 임포트!! 연습!
info() # 모듈 임포트!! 연습!
info() # 모듈 임포트!! 연습!
print()


 