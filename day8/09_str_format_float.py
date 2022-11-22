
'''
* 실수 포맷팅문자 %f

- 실수 포맷팅 서식문자 %f는 기본으로 소수점 6자리까지 표현하도록 
  설정되어 있습니다.

- 만약 자리수를 조절하고 싶다면 %.[자리수]f로 자리를 지정합니다.
'''

pi = 3.14159256
f = 5.56

print("원주율 값은 %f이고, 정수값은 %d이고, f의 값은 %f입니다." % (pi, pi, f))
# 원주율 값은 3.141593이고, 정수값은 3이고, f의 값은 5.560000입니다.
print("원주율의 값은 %.8f입니다." % pi)
print("원주율의 값은 %.11f입니다." % pi) # 원주율의 값은 3.14159256000
print("원주율의 값은 %.2f입니다." % pi)
print("f의 값은 %.2f입니다." % f)
print("f의 값은 %.1f입니다." % f) # 5.56 반올림해서 5.6
print("f의 값은 %.0f입니다." % f)


kor = 98
eng = 100
math = 80

# 평균은 소수점 2자리까지 표현!
sum = kor+eng+math
avg = sum / 3
print("총점: %d점, 평균: %.2f점" % (sum, avg))




