

'''
* 문자열 분할 메서드 split() 과 join

- split메서드는 구분자를 기준으로 문자열을 분할하여 리스트[]에
 저장한 뒤 반환합니다.
- 구분자를 지정할 때는 문자열로 지정해야 합니다.
'''
s1 = "떡볶이 김말이 닭강정"
print(s1.split()) # 괄호 안을 비우면 공백을 구분자로 하여 분할
                  # ['떡볶이', '김말이', '닭강정']

s2 = "서울->대전->대구->부산"
city = s2.split("->")
print(type(city)) # <class 'list'>
print(city) # ['서울', '대전', '대구', '부산']

s3 = "홍길동 | 오렌지나무 | 2019년 1월"
data = s3.split("|")
print(data) # ['홍길동 ', ' 오렌지나무 ', ' 2019년 1월']

for a in data:
    print(a.strip())



print("-" * 40)

# 메서드 join
s4 = "^-^"
print(s4.join("안알랴줌ㅋ")) # "안알랴줌ㅋ" 사이사이에 s4를 넣는다

# 연습 - idol변수에 문자열 
# "방탄소년단, 아이즈원, 샤이니"가 
# 저장되어 있습니다.
# split을 이용해 각 가수이름을 추출한 뒤 
# for문을 사용하여 "사랑해!!"와 함께 3줄로 출력하세요.
print("-" * 40)
idol = "방탄소년단, 아이즈원, 샤이니"

singer = idol.split(", ")
print(singer,end="\n\n") # ['방탄소년단', '아이즈원', '샤아니']

for s in singer:
    print(s, "사랑해!!")




