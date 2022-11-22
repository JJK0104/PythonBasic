# 난 이름 충돌걱정 안 할건데?
# factorial이라는 이름을 가진 함수를 안 만들 거야 근데 매번 소속을 굳이 써야돼?
# math.을 붙이기 귀찮다
# 그럴 떄는 from math import factorial

# from (모듈명) import (data) 는 특정 모듈에서 특정 data만 데리고 오겠다
# 그럼 이제 소속을 안 밝혀도 됨

import math # 혹시 내가 다른 math 사용할 경우 대비 
from math import factorial, sqrt, pi # 이 세개는 자주 사용할 거라 math. 안 붙이고 소속없이 사용

print(factorial(5)) # 소속 없이 사용 가능
print(sqrt(3)) 
# pi = 3
print(pi) # 위에 pi = 3 적으면 pi = 3이 출력 되네 
print(math.log10(3))
print(math.gcd(12, 18)) #최대 공약수

print("-" * 40)  

import statistics as st # statistics 모듈 불러올 건데 너무 길어, 그래서 st로 부를래

points = [65, 75, 55] 
print("평균:", st.mean(points))
print("분산:", st.variance(points))
print("표준편차:", st.stdev(points))


from math import factorial as fac
  
print(fac(6))
print(factorial(6)) # 이게 정상 작동하는 이유는 위에 
                    # from math import factorial, sqrt, pi 때문이다. 이거 없으면 오류
 



