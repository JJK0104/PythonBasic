

'''
* 문자열 슬라이싱

- 문자열 내부의 데이터를 부분적으로 추출할 때 사용하는 방법입니다.
ex) 문자열데이터[begin:end:step]

- range함수처럼 시작인덱스는 포함하지만 끝인덱스는 포함하지 않습니다.
- 언어는 대부분 이상 ~ 미만 이다
'''
s = "python"
print(s[2:5:1]) # tho
print(s[1:4]) # step생략시 1로 처리 -> yth
print(s[3:]) # 3번인덱스부터 끝까지 추출 -> hon
print(s[:4]) # 처음부터 4번 미만까지 추출 -> pyth
print(s[-6]) # p
print(s[:-1]) #pytho #마지막 문자는 -1, 'python'을 예로 들면 s[-1] = n, s[-6]=p
'''
- 문자열을 슬라이싱할 때 [] 내부의 3번째 값으로 step을 지정하면
  해당 step만큼 건너뛰면서 읽은 후 추출합니다.
'''
week = "월화수목금토일"
print(week[:]) # 처음부터 끝까지
print(week[::2]) # 처음부터 끝까지 step = 2 -> 월수금일
print(week[1:6:2])# 화목토

print("-" * 40)
# 연습 - ssn이라는 변수에 주민번호를 입력받아
# 저장하고  ex) 960201-2342123 
# 문자열 슬라이싱을 통해 주민번호 앞자리와 
# 뒷자리를 따로 출력해보세요.
ssn = input("주민번호: ")
print(ssn[:6])
print(ssn[7:])

year = ssn[:2]
month = ssn[2:4]
day = ssn[4:6]

if ssn[7] == "1" or ssn[7] == "3":
    gender = "남자"
elif ssn[7] == "2" or ssn[7] == "4":
    gender = "여자"

print(year,"년도", month,"월",day,"일생")


if ssn[7] == "1" or ssn[7] == "2":
    age = 2019 - (1900 + int(year)) + 1
else:
    age = 2019 - (2000 + int(year)) + 1
print(age,"세", gender)





